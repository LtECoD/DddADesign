#! /bin/bash

# export CUDA_VISIBLE_DEVICES="2,3"

# coarse-grained
python source/fine-tunning.py \
    --seed 99 \
    --checkpoint nferruz/ProtGPT2 \
    \
    --train_file ./data/processed/IPR035105.fasta \
    --val_file ./data/processed/IPR032724.fasta \
    --cache_dir ./cache \
    \
    --lr 5e-5 \
    --block_size 256 \
    --epochs 5 \

# coarse-grained fine-tunning
python source/fine-tunning.py \
    --seed 99 \
    --checkpoint ./save/IPR035105 \
    \
    --train_file ./data/processed/meta2k.fasta \
    --val_file ./data/processed/IPR032724.fasta \
    --cache_dir ./cache \
    \
    --lr 5e-5 \
    --block_size 256 \
    --epochs 5 \

# fine-grained fine-tunning
python source/fine-tunning.py \
    --seed 99 \
    --checkpoint nferruz/ProtGPT2 \
    \
    --train_file ./data/processed/meta2k.fasta \
    --val_file ./data/processed/IPR032724.fasta \
    --cache_dir ./cache \
    \
    --lr 5e-5 \
    --block_size 256 \
    --epochs 10 \