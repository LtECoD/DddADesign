#! /bin/bash

python source/fine-tunning.py \
    --seed 99 \
    --checkpoint nferruz/ProtGPT2 \
    --save_dir ./save/coarse \
    \
    --train_file ./data/processed/IPR035105.txt \
    --val_file ./data/processed/IPR032724.txt \
    --cache_dir ./cache \
    \
    --lr 5e-5 \
    --block_size 128 \
    --epochs 3 \
