#! /bin/bash

export CUDA_VISIBLE_DEVICES="2,3"

python ./source/run_clm.py \
    --model_name_or_path nferruz/ProtGPT2 \
    --train_file ./data/processed/meta2k.fasta \
    --validation_file ./data/processed/IPR032724.fasta \
    --tokenizer_name nferruz/ProtGPT2 \
    --block_size 256 \
    --do_train \
    --do_eval \
    --output_dir ./save/clm \
    --overwrite_output_dir \
    --learning_rate 5e-5  \
    --cache_dir ./cache