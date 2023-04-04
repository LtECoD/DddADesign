#! /bin/bash

SELFDIR=./plot/1.align_score

# process datasets
for DATASET in IPR032724 IPR035105;
do
    python ${SELFDIR}/reprocess_fasta.py \
        --fasta ./data/processed/${DATASET}.fasta \
        --out ${SELFDIR}/seqs/${DATASET}.fasta
done

# process results
for MODELNAME in ProtGPT2 IPR035105 IPR035105+meta2k meta2k;
do
    python ${SELFDIR}/reprocess_fasta.py \
        --fasta ./result/${MODELNAME}.fasta \
        --out ${SELFDIR}/seqs/generated_${MODELNAME}.fasta
done
