import os
import random
import argparse
from weblogo import (
    read_seq_data,
    LogoData,
    LogoOptions,
    LogoFormat,
    pdf_formatter
)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--aligned_fasta", type=str)
    parser.add_argument("--out", type=str)
    parser.add_argument("--title", type=str)
    parser.add_argument("--start", type=int)
    parser.add_argument("--end", type=int)
    args = parser.parse_args()

    seqs = read_seq_data(open(args.aligned_fasta, "r"))
    logodata = LogoData.from_seqs(seqs)
    logooptions = LogoOptions()
    logooptions.title_font = "Cambria"
    logooptions.text_font = "Cambria"
    logooptions.title = args.title
    logooptions.stacks_per_line = 60
    # logooptions.color_scheme = "Chemistry" 
    if args.start is not None:
        logooptions.logo_start = args.start
    if args.end is not None:
        logooptions.logo_end = args.end
    logoformat = LogoFormat(logodata, logooptions)
    pdf = pdf_formatter(logodata, logoformat)

    with open(args.out, "wb") as f:
        f.write(pdf)