import os
import random
import argparse
from Bio import SeqIO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int)
    parser.add_argument("--fasta", type=str)
    parser.add_argument("--selected_num", type=int)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()
    random.seed(args.seed)

    records = list(SeqIO.parse(args.fasta, "fasta"))
    selected_num = min(args.selected_num, len(records))
    records = random.sample(records, k=selected_num)
    SeqIO.write(records, args.out, "fasta")

