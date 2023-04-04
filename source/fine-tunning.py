import os
import math
import logging
import argparse
import evaluate
from itertools import chain
from datasets import load_dataset
from transformers import (
    set_seed,
    TrainingArguments,
    Trainer,
    default_data_collator,
    AutoTokenizer,
    AutoModelForCausalLM
)


metric = evaluate.load("accuracy")
logger = logging.getLogger(__name__)


def preprocess_logits_for_metrics(logits, labels):
    if isinstance(logits, tuple):
        # Depending on the model and config, logits may contain extra tensors,
        # like past_key_values, but logits always come first
        logits = logits[0]
    return logits.argmax(dim=-1)


def compute_metrics(eval_preds):
    preds, labels = eval_preds
    labels = labels[:, 1:].reshape(-1)
    preds = preds[:, :-1].reshape(-1)
    return metric.compute(predictions=preds, references=labels)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int)
    parser.add_argument("--save_dir", type=str, default="./save")
    parser.add_argument("--checkpoint", type=str)
    parser.add_argument("--train_file", type=str)
    parser.add_argument("--val_file", type=str)
    parser.add_argument("--block_size", type=int)
    parser.add_argument("--cache_dir", type=str)
    parser.add_argument("--lr", type=float)
    parser.add_argument("--epochs", type=int)
    parser.add_argument("--log_dir", type=str, default="./log")
    args = parser.parse_args()
    set_seed(args.seed)

    # re-direct checkpoint path and save directory
    model_name = os.path.basename(args.checkpoint)
    suffix = ""
    if os.path.exists(args.checkpoint):
        suffix = os.path.basename(args.checkpoint) + "+"
        assert os.path.isdir(args.checkpoint)
        for sub_path in os.listdir(args.checkpoint):
            if sub_path.startswith("checkpoint"):
                args.checkpoint = os.path.join(args.checkpoint, sub_path)
                break
    suffix = suffix + os.path.basename(args.train_file).split('.')[0]
    args.save_dir = os.path.join(args.save_dir, suffix)

    # tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint, cache_dir=args.cache_dir, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint, cache_dir=args.cache_dir, local_files_only=True)
    n_params = sum({p.data_ptr(): p.numel() for p in model.parameters()}.values())
    logger.info(f"Training new model from scratch - Total size={n_params/2**20:.2f}M params")

    # dataset
    def group_texts(examples):
        # Concatenate all texts.
        concatenated_examples = {k: list(chain(*examples[k])) for k in examples.keys()}
        total_length = len(concatenated_examples[list(examples.keys())[0]])
        # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can
        # customize this part to your needs.
        if total_length >= block_size:
            total_length = (total_length // block_size) * block_size
        # Split by chunks of max_len.
        result = {
            k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
            for k, t in concatenated_examples.items()
        }
        result["labels"] = result["input_ids"].copy()
        return result
    
    data_files = {"train": args.train_file, "val": args.val_file}
    raw_datasets = load_dataset(
        "text",
        data_files=data_files,
        cache_dir=args.cache_dir,
        keep_linebreaks=True)
    column_names = raw_datasets['train'].features
    tokenized_datasets = raw_datasets.map(
        lambda x: tokenizer(x["text"]), batched=True,
        remove_columns=column_names)
    block_size = args.block_size
    lm_datasets = tokenized_datasets.map(
        group_texts,
        batched=True)
    trainset = lm_datasets['train']
    valset = lm_datasets['val']

    # training
    ft_args = TrainingArguments(
        output_dir=args.save_dir,
        evaluation_strategy="epoch",
        learning_rate=args.lr,
        num_train_epochs=args.epochs,
        logging_dir=args.log_dir,
        logging_steps=50,
        save_strategy='epoch',
        seed=args.seed)

    trainer = Trainer(
        model=model,
        args=ft_args,
        train_dataset=trainset,
        eval_dataset=valset,
        tokenizer=tokenizer,
        data_collator=default_data_collator,
        compute_metrics=compute_metrics,
        preprocess_logits_for_metrics=preprocess_logits_for_metrics)

    train_result = trainer.train()
    trainer.save_model()
    metrics = train_result.metrics
    metrics["train_samples"] = len(trainset)
    trainer.log_metrics("train", metrics)
    trainer.save_metrics("train", metrics)
    trainer.save_state()

    logger.info("*** Evaluate ***")
    metrics = trainer.evaluate()
    metrics["eval_samples"] = len(valset)
    try:
        perplexity = math.exp(metrics["eval_loss"])
    except OverflowError:
        perplexity = float("inf")
    metrics["perplexity"] = perplexity
    trainer.log_metrics("eval", metrics)
    trainer.save_metrics("eval", metrics)
