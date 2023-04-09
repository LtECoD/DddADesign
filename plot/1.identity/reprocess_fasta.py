import os
import argparse
from Bio import SeqIO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", type=str)
    parser.add_argument("--tsv", type=str,
                        help="only for raw interpro fastas, to extract domain sequence")
    parser.add_argument("--extend", type=int,
                        help="residues extend on the side")
    parser.add_argument("--remove_duplicate", action="store_true")
    parser.add_argument("--extra_fasta", type=str,
                        help="add addtional active sequences")
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    seq_record = SeqIO.parse(args.fasta, format="fasta")
    id_seq_dict = {}
    for idx, record in enumerate(seq_record):
        _id = record.name.split("|")[0].strip()
        id_seq_dict[_id] = str(record.seq)

    data = []
    if args.tsv is not None:
        # for raw data downloaded from interpro
        if args.extend is None:
            args.extend = 0
        with open(args.tsv, "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                items = line.strip().split("\t")
                _id = items[0]
                if "," in items[-1]:
                    continue        # skip sequences with more than 1 segments
                _start, _end = map(int, items[-1].split(".."))
                sequence = id_seq_dict[_id]
                
                _start = max(_start-args.extend, 1)
                _end = min(_end+args.extend, len(sequence))
                domain_seq = sequence[_start-1: _end]

                data.append((_id, domain_seq))
    else:
        data = [(_id, seq) for _id, seq in id_seq_dict.items()]
    
    # add extra sequences
    extra_data = []
    if args.extra_fasta is not None:
        seq_record = SeqIO.parse(args.extra_fasta, format="fasta")
        for idx, record in enumerate(seq_record):
            _id = record.name.split("|")[0].strip()
            extra_data.append((_id, str(record.seq)))
    data.extend(extra_data)
    
    # remove duplicate in reverse order
    if args.remove_duplicate:
        _data = [] 
        dataset = set()
        for _id, seq in data[::-1]:
            if seq in dataset:
                continue
            dataset.add(seq)
            _data.append((_id, seq))
        data = _data[::-1]


    data = [f">{_id}\n"+seq+"\n" for _id, seq in data]
    with open(args.out, "w") as f:
        f.writelines(data)