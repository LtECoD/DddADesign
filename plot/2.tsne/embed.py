import os
import re
import torch
import shutil
import argparse
import numpy as np
import torch.nn as nn

from transformers import T5EncoderModel, T5Tokenizer
from transformers import BertModel, BertTokenizer
from transformers import XLNetModel, XLNetTokenizer
from transformers import AlbertModel, AlbertTokenizer


def build_pretrained_model(model_name):
    if "t5" in model_name:
        tokenizer = T5Tokenizer.from_pretrained(model_name, do_lower_case=False)
        model = T5EncoderModel.from_pretrained(model_name)
    elif "albert" in model_name:
        tokenizer = AlbertTokenizer.from_pretrained(model_name, do_lower_case=False)
        model = AlbertModel.from_pretrained(model_name)
    elif "bert" in model_name:
        tokenizer = BertTokenizer.from_pretrained(model_name, do_lower_case=False)
        model = BertModel.from_pretrained(model_name)
    elif "xlnet" in model_name:
        tokenizer = XLNetTokenizer.from_pretrained(model_name, do_lower_case=False )
        model = XLNetModel.from_pretrained(model_name)
    else:
        raise ValueError(f"Unkown model name: {model_name}")
    return tokenizer, model


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretrained_model", type=str)
    parser.add_argument("--device", type=int)
    parser.add_argument("--batch_size", type=int)
    parser.add_argument("--fasta", type=str)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    # load model
    print(f">>>>> load pretrained language model {args.pretrained_model}")
    tokenizer, embeder = build_pretrained_model(args.pretrained_model)
    embeder = embeder.eval()
    if args.device is not None:
        embeder = embeder.to(args.device)
    
    # read file
    samples = []
    with open(args.fasta, "r") as f:
        lines = f.readlines()
        for idx in range(0, len(lines), 2):
            _id = lines[idx].strip()[1:]
            seq = lines[idx+1].strip()
            seq = re.sub(r"[UZOB]", "X", seq)
            samples.append((_id, seq))

    # emb
    embeds = []
    def process_buffer():
        pros = [s[0].strip() for s in buffer]
        seqs = [" ".join(s[1]) for s in buffer]

        inputs = tokenizer.batch_encode_plus(seqs, add_special_tokens=True, padding=True)
        if args.device is not None:
            inputs = {k: torch.tensor(v).to(args.device) for k, v in inputs.items()}
        else:
            inputs = {k: torch.tensor(v) for k, v in inputs.items()}
        with torch.no_grad():
            embedding = embeder(**inputs)
        embedding = embedding.last_hidden_state.cpu().numpy()
        assert len(seqs) == len(pros) == len(embedding)

        for idx in range(len(embedding)):
            seq_len = (inputs['attention_mask'][idx] == 1).sum()
            if seq_len - 1 == len(seqs[idx].strip().split()):
                seq_emb = embedding[idx][:seq_len-1]
            elif seq_len - 2 == len(seqs[idx].strip().split()):
                seq_emb = embedding[idx][1:seq_len-1]
            pool_seq_emb = np.mean(seq_emb, axis=0)
            embeds.append(pool_seq_emb)
            # np.save(os.path.join(args.out, pros[idx]+".npy"), pool_seq_emb)

    buffer = []
    processed_num = 0
    for idx, (pro, seq) in enumerate(samples):
        buffer.append((pro, seq))
        if len(buffer) >= args.batch_size:
            process_buffer()
            processed_num += len(buffer)
            buffer = []

    if len(buffer) > 0:
        process_buffer()
        processed_num += len(buffer)
        buffer = []
    np.save(args.out, np.vstack(embeds))
    print(f">>>>> Processed {processed_num} proteins.")