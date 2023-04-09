#! /bin/bash
SELFDIR=./plot/2.umap
# python ${SELFDIR}/umap_reduce.py \
#     --emb_dir ${SELFDIR}/embs_prott5 \
#     --model_name ProtGPT2 IPR035105 IPR035105+meta2k meta2k IPR032724r\
#     --active_num 18 \
#     --out ${SELFDIR}/plot_data_prott5.csv

python ${SELFDIR}/umap_reduce.py \
    --emb_dir ${SELFDIR}/embs_protbert \
    --model_name ProtGPT2 IPR035105 IPR035105+meta2k meta2k IPR032724r\
    --active_num 18 \
    --out ${SELFDIR}/plot_data_protbert.csv