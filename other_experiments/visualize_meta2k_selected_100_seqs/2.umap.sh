#! /bin/bash
SELFDIR=./other_experiments/visualize_meta2k_selected_100_seqs

python ${SELFDIR}/umap_reduce.py \
    --emb_dir ${SELFDIR}/embs_prott5 \
    --datasets selected_100_seq IPR032724 \
    --active_num 16 \
    --out ${SELFDIR}/plot_data_prott5_umap.csv

python ${SELFDIR}/umap_reduce.py \
    --emb_dir ${SELFDIR}/embs_protbert \
    --datasets selected_100_seq IPR032724 \
    --active_num 16 \
    --out ${SELFDIR}/plot_data_protbert_umap.csv