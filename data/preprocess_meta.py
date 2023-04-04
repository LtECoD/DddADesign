import argparse
from Bio import SeqIO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--faa", type=str)
    parser.add_argument("--out", type=str)
    parser.add_argument("--len_per_line", type=int, default=60)

    args = parser.parse_args()

    seq_record = SeqIO.parse(args.faa, format="fasta")
    data = []
    for idx, record in enumerate(seq_record):
        seq = str(record.seq)
        seq = "\n".join([
                seq[i: i+args.len_per_line] \
                    for i in range(0, len(seq), args.len_per_line)])

        data.append("<|endoftext|>\n"+seq+"\n")

    with open(args.out, "w") as f:
        f.writelines(data)