#! /bin/bash

SELF_DIR=./other_experiments/visualize_meta2k_selected_100_seqs

python ${SELF_DIR}/meta2k_selected_seqs.py \
    --meta2k_fasta data/raw/DddA_V4_hmm_PF14428.8_E10_filteredHits_all_CorrEnvs_derep.faa \
    --selected_ids ${SELF_DIR}/seqs/selected_100_ids.txt \
    --out ${SELF_DIR}/seqs/selected_100_seq.fasta