#! /bin/bash
SELFDIR=./plot/1.identity

python ${SELFDIR}/plot.py \
    --data_dir ${SELFDIR}/plot_data \
    --out ${SELFDIR}/identity.pdf \
    --model_name IPR002125+IPR035105+meta2k IPR035105+meta2k
    # --model_name ProtGPT2 IPR035105 IPR035105+meta2k meta2k \