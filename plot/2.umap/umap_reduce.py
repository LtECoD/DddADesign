import os
import argparse
import numpy as np
import pandas as pd
import umap


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--emb_dir", type=str)
    parser.add_argument("--model_name", nargs="+")
    parser.add_argument("--active_num", type=int)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    data = []
    labels = []
    for model in args.model_name:
        embs = np.load(os.path.join(args.emb_dir, model+".npy"))
        data.append(embs)
        labels.extend([model]*embs.shape[0])
    data = np.vstack(data)

    # active sequences
    if args.active_num is not None:
        labels[-args.active_num:] = ["Active"] * args.active_num

    data_reduced = umap.UMAP(min_dist=0.3).fit_transform(data)

    df = pd.DataFrame(columns=["Dim1", "Dim2", "Label"])
    df["Dim1"] = data_reduced[:, 0]
    df["Dim2"] = data_reduced[:, 1]
    df["Label"] = labels
    df.to_csv(args.out, index=False)


