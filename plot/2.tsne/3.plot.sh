#! /bin/bash

SELFDIR=./plot/2.tsne

python ${SELFDIR}/plot.py \
    --data ${SELFDIR}/plot_data_prott5.csv \
    --out ${SELFDIR}/tsne_prott5.pdf

python ${SELFDIR}/plot.py \
    --data ${SELFDIR}/plot_data_protbert.csv \
    --out ${SELFDIR}/tsne_protbert.pdf