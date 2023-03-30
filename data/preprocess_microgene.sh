#!/bin/bash

python ./data/preprocess_microgene.py \
    --faa ./data/raw/DddA_V4_hmm_PF14428.8_E10_filteredHits_all_CorrEnvs_derep.faa \
    --out ./data/processed/micro-2k.txt 