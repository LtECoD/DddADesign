#! /bin/bash

SELFDIR=./other_experiments/visualize_meta2k_selected_100_seqs

python ${SELFDIR}/plot.py \
    --data ${SELFDIR}/plot_data_prott5_umap.csv \
    --out ${SELFDIR}/umap_prott5.pdf

python ${SELFDIR}/plot.py \
    --data ${SELFDIR}/plot_data_protbert_umap.csv \
    --out ${SELFDIR}/umap_protbert.pdf