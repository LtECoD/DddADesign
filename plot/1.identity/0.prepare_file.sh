#! /bin/bash

SELFDIR=./plot/1.identity

# # process datasets
# DATASET=IPR035105;
# python ${SELFDIR}/reprocess_fasta.py \
#     --fasta ./data/raw/protein-matching-${DATASET}.fasta \
#     --tsv ./data/raw/protein-matching-${DATASET}.tsv \
#     --extend 50 \
#     --remove_duplicate \
#     --out ${SELFDIR}/seqs/${DATASET}.fasta

# DATASET=IPR032724
# python ${SELFDIR}/reprocess_fasta.py \
#     --fasta ./data/raw/protein-matching-${DATASET}.fasta \
#     --tsv ./data/raw/protein-matching-${DATASET}.tsv \
#     --extend 50 \
#     --remove_duplicate \
#     --extra_fasta ./data/raw/active_sequences.fasta \
#     --out ${SELFDIR}/seqs/${DATASET}.fasta

# process results
# for MODELNAME in ProtGPT2 IPR035105 IPR035105+meta2k meta2k;
for MODELNAME in IPR002125 IPR002125+IPR035105 IPR002125+IPR035105+meta2k;
do
    python ${SELFDIR}/reprocess_fasta.py \
        --fasta ./result/${MODELNAME}.fasta \
        --remove_duplicate \
        --out ${SELFDIR}/seqs/generated_${MODELNAME}.fasta
done
