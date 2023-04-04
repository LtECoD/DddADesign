import os
import argparse
from transformers import (
    set_seed,
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
    TextGenerationPipeline
)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int)
    parser.add_argument("--cache_dir", type=str)
    parser.add_argument("--checkpoint", type=str)
    parser.add_argument("--result_dir", type=str)
    parser.add_argument("--max_length", type=int)
    parser.add_argument("--seq_num", type=int)
    args = parser.parse_args()
    set_seed(args.seed)

    # re-direct checkpoint path
    model_name = os.path.basename(args.checkpoint)

    # tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint, cache_dir=args.cache_dir, local_files_only=True)
    fine_tuned_model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint, cache_dir=args.cache_dir, local_files_only=True)
    pipe = pipeline(
        "text-generation", model=fine_tuned_model, tokenizer=tokenizer)

    # generate
    sequences = pipe("<|endoftext|>", 
                     max_length=args.max_length, 
                     do_sample=True, 
                     top_k=950, 
                     repetition_penalty=1.2, 
                     num_return_sequences=args.seq_num,
                     eos_token_id=0)

    # write into fasta
    idx = 0
    lines = []
    for seq in sequences:
        line = seq['generated_text']
        assert line.startswith("<|endoftext|>")
        trunc_line = "\n" + line[13:].strip() + "\n"
        if len(trunc_line) < 10:
            continue
        lines.append(f">{model_name}-{idx}" + trunc_line)
        idx += 1

    with open(os.path.join(args.result_dir, model_name+".fasta"), "w") as f:
        f.writelines(lines) 