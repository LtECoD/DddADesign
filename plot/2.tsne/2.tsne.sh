#! /bin/bash
SELFDIR=./plot/2.tsne
python ${SELFDIR}/tsne.py \
    --emb_dir ${SELFDIR}/embs \
    --model_name IPR032724r ProtGPT2 IPR035105 IPR035105+meta2k meta2k \
    --out ${SELFDIR}/plot_data.csv