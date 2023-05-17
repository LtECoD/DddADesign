#! /bin/bash

# export CUDA_VISIBLE_DEVICES="2,3"

# # validate protgpt2
# python source/fine-tunning.py \
#     --seed 99 \
#     --checkpoint nferruz/ProtGPT2 \
#     \
#     --train_file ./data/processed/IPR032724.fasta \
#     --val_file ./data/processed/IPR032724.fasta \
#     --cache_dir ./cache \
#     \
#     --lr 5e-5 \
#     --block_size 256 \
#     --epochs 0 \

# IPR002125
python source/fine-tunning.py \
    --seed 99 \
    --checkpoint nferruz/ProtGPT2 \
    \
    --train_file ./data/processed/IPR002125.fasta \
    --val_file ./data/processed/IPR032724.fasta \
    --cache_dir ./cache \
    \
    --lr 5e-6 \
    --block_size 256 \
    --epochs 5 \

# IPR002125 + IPR035105
python source/fine-tunning.py \
    --seed 99 \
    --checkpoint ./save/IPR002125 \
    \
    --train_file ./data/processed/IPR035105.fasta \
    --val_file ./data/processed/IPR032724.fasta \
    --cache_dir ./cache \
    \
    --lr 5e-6 \
    --block_size 256 \
    --epochs 10 \

# IPR002125 + IPR035105 + meta2k
python source/fine-tunning.py \
    --seed 99 \
    --checkpoint ./save/IPR002125+IPR035105 \
    \
    --train_file ./data/processed/meta2k.fasta \
    --val_file ./data/processed/IPR032724.fasta \
    --cache_dir ./cache \
    \
    --lr 5e-5 \
    --block_size 256 \
    --epochs 10 \


# # coarse-grained
# python source/fine-tunning.py \
#     --seed 99 \
#     --checkpoint nferruz/ProtGPT2 \
#     \
#     --train_file ./data/processed/IPR035105.fasta \
#     --val_file ./data/processed/IPR032724.fasta \
#     --cache_dir ./cache \
#     \
#     --lr 5e-6 \
#     --block_size 256 \
#     --epochs 10 \

# python source/fine-tunning.py \
#     --seed 99 \
#     --checkpoint ./save/IPR035105 \
#     \
#     --train_file ./data/processed/meta2k.fasta \
#     --val_file ./data/processed/IPR032724.fasta \
#     --cache_dir ./cache \
#     \
#     --lr 5e-5 \
#     --block_size 256 \
#     --epochs 10 \

# python source/fine-tunning.py \
#     --seed 99 \
#     --checkpoint nferruz/ProtGPT2 \
#     \
#     --train_file ./data/processed/meta2k.fasta \
#     --val_file ./data/processed/IPR032724.fasta \
#     --cache_dir ./cache \
#     \
#     --lr 5e-5 \
#     --block_size 256 \
#     --epochs 10 \