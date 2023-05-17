#!/bin/bash

# # minning 5k bitscore 10
# python ./data/preprocess_meta.py \
#     --faa ./data/raw/DddA_V4_nofilter_CorrEnvs.faa \
#     --out ./data/processed/meta5k.fasta

# # minning 4k bitscore 25
# python ./data/preprocess_meta.py \
#     --faa ./data/raw/DddA_V4_filtered_all_CorrEnvs.faa \
#     --out ./data/processed/meta4k.fasta

# # filter final 2k
# python ./data/preprocess_meta.py \
#     --faa ./data/raw/DddA_V4_hmm_PF14428.8_E10_filteredHits_all_CorrEnvs_derep.faa \
#     --out ./data/processed/meta2k.fasta

# active
python ./data/preprocess_meta.py \
    --faa ./data/raw/active_sequences.fasta \
    --out ./data/processed/active.fasta