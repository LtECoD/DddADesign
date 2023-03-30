import argparse
from Bio import SeqIO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--faa", type=str)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    seq_record = SeqIO.parse(args.faa, format="fasta")
    data = []
    for idx, record in enumerate(seq_record):
        data.append("<|endoftext|>"+str(record.seq)+"\n")


    with open(args.out, "w") as f:
        f.writelines(data)