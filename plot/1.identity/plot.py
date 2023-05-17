import os
import argparse
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str)
    parser.add_argument("--model_name", nargs="+")
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    df = pd.DataFrame(columns=["Model", "Overlap Length", "Identity", "BS"])

    models_num = len(args.model_name) + 1
    for name in args.model_name:
        lines = open(os.path.join(args.data_dir, name+".csv"), "r").readlines()
        for l in lines:
            _overlen, _iden, _bs = l.strip().split("\t")
            _overlen, _iden, _bs = int(_overlen), float(_iden), float(_bs)

            df.loc[len(df)] = {"Model": name, 
                            "Overlap Length": _overlen, 
                            "Identity": _iden,
                            "BS": _bs}

    print(df)

    font_size = 14
    font_path = "/lustre/home/yangsen/Cambria.ttf"
    font = matplotlib.font_manager.FontProperties(fname=font_path)

    sns.set()
    plt.style.use("ggplot")
    # sns.set_style("ticks")
    
    g = sns.scatterplot(
        x="Overlap Length",
        y="Identity",
        hue="Model",
        size="BS",
        data=df)

    x_labels = g.get_xticklabels()
    y_labels = g.get_yticklabels()
    for _label in x_labels + y_labels:
        _label.set_fontproperties(font)
    plt.ylabel("Identity", fontproperties=font, fontsize=12)
    plt.xlabel("Overlap Length", fontproperties=font, fontsize=12)
    
    handles, labels = g.get_legend_handles_labels()
    legends = g.legend(handles=handles[:models_num], labels=labels[:models_num], frameon=False).get_texts()
    for leg in legends:
        leg.set_fontproperties(font)
        # leg.set_size(15)

    sns.despine()
    plt.savefig(args.out, bbox_inches='tight')

