#! /bin/bash

SELFDIR=./plot/3.seqlogo

cp ./data/raw/active_sequences.fasta ./plot/3.seqlogo/seqs

for MODELNAME in IPR035105 IPR035105+meta2k meta2k ;
do
    python ${SELFDIR}/select_generated_seqs.py \
        --seed 100 \
        --fasta ./result/${MODELNAME}.fasta \
        --selected_num 100 \
        --out ${SELFDIR}/seqs/generated_${MODELNAME}.fasta
done