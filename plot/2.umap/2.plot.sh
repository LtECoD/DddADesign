#! /bin/bash

SELFDIR=./plot/2.umap

# python ${SELFDIR}/plot.py \
#     --data ${SELFDIR}/plot_data_prott5.csv \
#     --out ${SELFDIR}/umap_prott5.pdf

python ${SELFDIR}/plot.py \
    --data ${SELFDIR}/plot_data_protbert.csv \
    --out ${SELFDIR}/umap_protbert.pdf