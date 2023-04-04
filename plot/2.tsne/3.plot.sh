#! /bin/bash

SELFDIR=./plot/2.tsne

python ${SELFDIR}/plot.py \
    --data ${SELFDIR}/plot_data.csv \
    --out ${SELFDIR}/tsne.pdf