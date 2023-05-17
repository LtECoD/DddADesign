#!/bin/bash

# IPR002125
python ./data/preprocess_interpro.py \
    --fasta ./data/raw/protein-matching-IPR002125.fasta \
    --tsv ./data/raw/protein-matching-IPR002125.tsv \
    --out ./data/processed/IPR002125.fasta \
    --extend 50

# IPR032724 DddA-like 500+
python ./data/preprocess_interpro.py \
    --fasta ./data/raw/protein-matching-IPR032724.fasta \
    --tsv ./data/raw/protein-matching-IPR032724.tsv \
    --out ./data/processed/IPR032724.fasta \
    --extend 50

# IPR035105 Deoxycytidylate deaminase domain, 2w+
python ./data/preprocess_interpro.py \
    --fasta ./data/raw/protein-matching-IPR035105.fasta \
    --tsv ./data/raw/protein-matching-IPR035105.tsv \
    --out ./data/processed/IPR035105.fasta \
    --extend 50

# IPR002125 Cytidine and deoxycytidylate deaminase domain, 18w+
python ./data/preprocess_interpro.py \
    --fasta ./data/raw/protein-matching-IPR002125.fasta \
    --tsv ./data/raw/protein-matching-IPR002125.tsv \
    --out ./data/processed/IPR002125.fasta \
    --extend 50