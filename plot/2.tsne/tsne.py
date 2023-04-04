import os
import argparse
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--emb_dir", type=str)
    parser.add_argument("--model_name", nargs="+")
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    data = []
    labels = []
    for model in args.model_name:
        embs = np.load(os.path.join(args.emb_dir, model+".npy"))
        data.append(embs)
        labels.extend([model]*embs.shape[0])
    data = np.vstack(data)

    data_reduced = TSNE(
        n_components=2,
        perplexity=50,
        learning_rate=200,
        n_iter=2000).fit_transform(data)
    
    df = pd.DataFrame(columns=["Dim1", "Dim2", "Label"])
    df["Dim1"] = data_reduced[:, 0]
    df["Dim2"] = data_reduced[:, 1]
    df["Label"] = labels
    df.to_csv(args.out, index=False)


