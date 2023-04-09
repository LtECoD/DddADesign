#! /bin/bash

SELFDIR=./plot/2.tsne
PTLM=Rostlab/prot_t5_xl_uniref50

for MODELNAME in ProtGPT2 IPR035105 IPR035105+meta2k meta2k;
do
    python ${SELFDIR}/embed.py \
        --pretrained_model ${PTLM} \
        --device 0 \
        --batch_size 32 \
        --fasta ${SELFDIR}/seqs/generated_${MODELNAME}.fasta \
        --out ${SELFDIR}/embs_prott5/${MODELNAME}.npy
done

python ${SELFDIR}/embed.py \
    --pretrained_model ${PTLM} \
    --device 0 \
    --batch_size 32 \
    --fasta ${SELFDIR}/seqs/IPR032724.fasta \
    --out ${SELFDIR}/embs_prott5/IPR032724r.npy


# PTLM=Rostlab/prot_bert
# for MODELNAME in ProtGPT2 IPR035105 IPR035105+meta2k meta2k;
# do
#     python ${SELFDIR}/embed.py \
#         --pretrained_model ${PTLM} \
#         --device 0 \
#         --batch_size 32 \
#         --fasta ${SELFDIR}/seqs/generated_${MODELNAME}.fasta \
#         --out ${SELFDIR}/embs_protbert/${MODELNAME}.npy
# done

# python ${SELFDIR}/embed.py \
#     --pretrained_model ${PTLM} \
#     --device 0 \
#     --batch_size 32 \
#     --fasta ${SELFDIR}/seqs/IPR032724.fasta \
#     --out ${SELFDIR}/embs_protbert/IPR032724r.npy
