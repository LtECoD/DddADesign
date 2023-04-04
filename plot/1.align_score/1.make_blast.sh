#! /bin/bash

SELFDIR=./plot/1.align_score

# make blast db from fasta file
DBFASTA=IPR032724
makeblastdb \
    -in ${SELFDIR}/seqs/${DBFASTA}.fasta \
    -dbtype prot \
    -out ${SELFDIR}/seqdb/${DBFASTA}

# # blast align file
for MODELNAME in ProtGPT2 IPR035105 IPR035105+meta2k meta2k;
do
    blastp \
        -query ${SELFDIR}/seqs/generated_${MODELNAME}.fasta \
        -out ${SELFDIR}/blast_result/${MODELNAME}.blast \
        -db ${SELFDIR}/seqdb/${DBFASTA} \
        -outfmt 6 \
        -num_threads 16 \
        -max_target_seqs 1 \
        -evalue 1e-2      #! evalue lower than 1e-4 is good
done

# extract info
for MODELNAME in ProtGPT2 IPR035105 IPR035105+meta2k meta2k;
do
    python ${SELFDIR}/extract_blast_info.py \
        --blast ${SELFDIR}/blast_result/${MODELNAME}.blast \
        --out ${SELFDIR}/plot_data/${MODELNAME}.csv
done
