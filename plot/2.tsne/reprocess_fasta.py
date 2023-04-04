import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    data_name = os.path.basename(args.fasta).split(".")[0]
    
    fasta_lines = open(args.fasta, "r").readlines()
    fasta_lines = [f">{data_name}-{idx}\n" if l.strip() == "<|endoftext|>" else l for idx, l in enumerate(fasta_lines)]

    data = []
    idx = -1
    for line in fasta_lines:
        if line.startswith(">"):
            if idx >= 0:
                data[idx] = data[idx] + "\n"
            idx += 1
            data.append(line)
        else:
            data[idx] = data[idx] + line.strip()
    
    with open(args.out, "w") as f:
        f.writelines(data)