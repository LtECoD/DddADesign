#! /bin/bash

SELFDIR=./plot/3.seqlogo

python ${SELFDIR}/seqlogo.py \
    --aligned_fasta ${SELFDIR}/align/active_sequences_align.fasta\
    --out ${SELFDIR}/active.pdf \
    --title "Active Sequence" \
    --start 120


python ${SELFDIR}/seqlogo.py \
    --aligned_fasta ${SELFDIR}/align/generated_meta2k_align.fasta\
    --out ${SELFDIR}/meta2k.pdf \
    --title "Meta2K" \
    --start 440 \
    --end 580


python ${SELFDIR}/seqlogo.py \
    --aligned_fasta ${SELFDIR}/align/generated_IPR035105+meta2k_align.fasta\
    --out ${SELFDIR}/IPR035105+meta2k.pdf \
    --title "IPR035105+meta2k" \
    --start 297 \
    --end 455

python ${SELFDIR}/seqlogo.py \
    --aligned_fasta ${SELFDIR}/align/generated_IPR035105_align.fasta\
    --out ${SELFDIR}/IPR035105.pdf \
    --title "IPR035105" \
    --start 40 \
    --end 340

python ${SELFDIR}/seqlogo.py \
    --aligned_fasta ${SELFDIR}/align/generated_ProtGPT2_align.fasta\
    --out ${SELFDIR}/ProtGPT2.pdf \
    --title "ProtGPT2" \
    --start 40 \
    --end 340
    