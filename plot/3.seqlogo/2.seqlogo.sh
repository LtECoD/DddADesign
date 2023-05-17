#! /bin/bash

SELFDIR=./plot/3.seqlogo

# python ${SELFDIR}/seqlogo.py \
#     --aligned_fasta ${SELFDIR}/align/active_sequences_align.fasta\
#     --out ${SELFDIR}/active.pdf \
#     --title "Active Sequence" \
#     # --start 120


for MODELNAME in IPR035105 IPR035105+meta2k meta2k ;
do
    python ${SELFDIR}/seqlogo.py \
        --aligned_fasta ${SELFDIR}/align/generated_${MODELNAME}_align.fasta\
        --out ${SELFDIR}/${MODELNAME}.pdf \
        --title "${MODELNAME}"
done



# python ${SELFDIR}/seqlogo.py \
#     --aligned_fasta ${SELFDIR}/align/generated_IPR035105+meta2k+IPR032724+active_align.fasta\
#     --out ${SELFDIR}/IPR035105+meta2k+IPR032724+active.pdf \
#     --title "IPR035105+meta2k+IPR032724+active" \
#     # --start 40 \
#     # --end 340

# python ${SELFDIR}/seqlogo.py \
#     --aligned_fasta ${SELFDIR}/align/generated_ProtGPT2_align.fasta\
#     --out ${SELFDIR}/ProtGPT2.pdf \
#     --title "ProtGPT2" \
#     --start 40 \
#     --end 340
    