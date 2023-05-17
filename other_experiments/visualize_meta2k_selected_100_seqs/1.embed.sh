#! /bin/bash

SELFDIR=./other_experiments/visualize_meta2k_selected_100_seqs
PTLM=Rostlab/prot_t5_xl_uniref50

python ${SELFDIR}/embed.py \
    --pretrained_model ${PTLM} \
    --device 0 \
    --batch_size 32 \
    --fasta ${SELFDIR}/seqs/IPR032724.fasta \
    --out ${SELFDIR}/embs_prott5/IPR032724.npy

python ${SELFDIR}/embed.py \
    --pretrained_model ${PTLM} \
    --device 0 \
    --batch_size 32 \
    --fasta ${SELFDIR}/seqs/selected_100_seq.fasta \
    --out ${SELFDIR}/embs_prott5/selected_100_seq.npy


PTLM=Rostlab/prot_bert
python ${SELFDIR}/embed.py \
    --pretrained_model ${PTLM} \
    --device 0 \
    --batch_size 32 \
    --fasta ${SELFDIR}/seqs/IPR032724.fasta \
    --out ${SELFDIR}/embs_protbert/IPR032724.npy

python ${SELFDIR}/embed.py \
    --pretrained_model ${PTLM} \
    --device 0 \
    --batch_size 32 \
    --fasta ${SELFDIR}/seqs/selected_100_seq.fasta \
    --out ${SELFDIR}/embs_protbert/selected_100_seq.npy
