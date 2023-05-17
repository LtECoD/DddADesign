#! /bin/bash

# export CUDA_VISIBLE_DEVICES="2,3"

# coarse-grained fine-tunning
# python source/generate.py \
#     --seed 99 \
#     --cache_dir ./cache \
#     --checkpoint nferruz/ProtGPT2 \
#     --max_length  80 \
#     --seq_num 500\
#     --result_dir ./result

python source/generate.py \
    --seed 99 \
    --cache_dir ./cache \
    --checkpoint ./save/IPR002125 \
    --max_length  80 \
    --seq_num 500 \
    --result_dir ./result

python source/generate.py \
    --seed 99 \
    --cache_dir ./cache \
    --checkpoint ./save/IPR002125+IPR035105 \
    --max_length  80 \
    --seq_num 500 \
    --result_dir ./result

python source/generate.py \
    --seed 99 \
    --cache_dir ./cache \
    --checkpoint ./save/IPR002125+IPR035105+meta2k \
    --max_length  80 \
    --seq_num 500 \
    --result_dir ./result

# python source/generate.py \
#     --seed 99 \
#     --cache_dir ./cache \
#     --checkpoint ./save/IPR035105 \
#     --max_length  80 \
#     --seq_num 500 \
#     --result_dir ./result

# python source/generate.py \
#     --seed 99 \
#     --cache_dir ./cache \
#     --checkpoint ./save/IPR035105+meta2k \
#     --max_length  80 \
#     --seq_num 500 \
#     --result_dir ./result

# python source/generate.py \
#     --seed 99 \
#     --cache_dir ./cache \
#     --checkpoint ./save/meta2k \
#     --max_length  80 \
#     --seq_num 500 \
#     --result_dir ./result

# clm
# python source/generate.py \
#     --seed 99 \
#     --cache_dir ./cache \
#     --checkpoint ./save/clm \
#     --max_length  80 \
#     --seq_num 10 \
#     --result_dir ./result