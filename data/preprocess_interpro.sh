#!/bin/bash

python ./data/preprocess_interpro.py \
    --fasta ./data/raw/protein-matching-IPR032724.fasta \
    --tsv ./data/raw/protein-matching-IPR032724.tsv \
    --out ./data/processed/IPR032724.txt 

python ./data/preprocess_interpro.py \
    --fasta ./data/raw/protein-matching-IPR035105.fasta \
    --tsv ./data/raw/protein-matching-IPR035105.tsv \
    --out ./data/processed/IPR035105.txt 