#! /bin/bash
SELFDIR=./plot/1.align_score

python ${SELFDIR}/plot.py \
    --data_dir ${SELFDIR}/plot_data \
    --model_name ProtGPT2 IPR035105 IPR035105+meta2k meta2k \
    --out ${SELFDIR}/identity.pdf