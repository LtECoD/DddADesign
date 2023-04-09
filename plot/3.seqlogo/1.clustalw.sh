#! /bin/bash

SELFDIR=./plot/3.seqlogo

clustalo -i ${SELFDIR}/seqs/active_sequences.fasta > ${SELFDIR}/align/active_sequences_align.fasta

for MODELNAME in ProtGPT2 IPR035105 IPR035105+meta2k meta2k;
do
    clustalo -i ${SELFDIR}/seqs/generated_${MODELNAME}.fasta > ${SELFDIR}/align/generated_${MODELNAME}_align.fasta
done