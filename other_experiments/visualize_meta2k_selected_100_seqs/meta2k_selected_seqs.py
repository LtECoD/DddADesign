import os
import argparse
from Bio import SeqIO
from copy import deepcopy


if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument("--meta2k_fasta", type=str)
   parser.add_argument("--selected_ids", type=str)
   parser.add_argument("--out", type=str)
   args = parser.parse_args()

   selected_ids = open(args.selected_ids, "r").readlines()
   selected_ids = [_id.strip().split() for _id in selected_ids]
   selected_ids = {t: r for t, r in selected_ids}

   records = SeqIO.parse(args.meta2k_fasta, format="fasta")
   records = {rec.id: rec for rec in records}

   selected_records = []
   for sid in selected_ids:
      assert sid in records

      _rec = deepcopy(records[sid])
      _rec.id = selected_ids[sid]
      _rec.description = ""
      selected_records.append(_rec)
   
   SeqIO.write(selected_records, args.out, "fasta")



      


      
   

