import argparse
from Bio import SeqIO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str)
    parser.add_argument("--tsv", type=str)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()


    seq_record = SeqIO.parse(args.fasta, format="fasta")
    id_seq_dict = {}
    for idx, record in enumerate(seq_record):
        _id = record.name.split("|")[0].strip()
        id_seq_dict[_id] = str(record.seq)

    data = []
    with open(args.tsv, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            items = line.strip().split("\t")
            _id = items[0]
            if "," in items[-1]:
                continue        # skip sequences with more than 1 segments 
            _start, _end = map(int, items[-1].split(".."))
            assert _id in id_seq_dict
            data.append("<|endoftext|>"+id_seq_dict[_id][_start-1: _end]+"\n")
    
    with open(args.out, "w") as f:
        f.writelines(data)