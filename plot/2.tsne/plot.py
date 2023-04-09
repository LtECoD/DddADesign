import os
import argparse
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    print(df)

    font_size = 14
    font_path = "/lustre/home/yangsen/Cambria.ttf"
    font = matplotlib.font_manager.FontProperties(fname=font_path)

    sns.set()
    plt.style.use("ggplot")
    # sns.set_style("ticks")
    
    g = sns.scatterplot(
        x="Dim1",
        y="Dim2",
        hue="Label",
        data=df,
        size=0.5)
    g.set_xticklabels([])
    g.set_yticklabels([])
    g.xaxis.label.set_visible(False)
    g.yaxis.label.set_visible(False)


    # activate sequences
    import math
    pi = math.pi
    activate_idx_name = [
        (-1, "DddA", 5, 15),
        (-5, "Q2L7", 5, -20),
        (-8, "FZY2", -30, -20),
        (-11, "SA071", 15, -20),
        (-12, "SA046", -30, 15),
        (-18, "SA093", -30, 15)
    ]
    for idx, name, tx, ty in activate_idx_name:
        _index = len(df) + idx
        x = df.loc[_index, "Dim1"]
        y = df.loc[_index, "Dim2"]
        g.annotate(
            text=name,
            xy=(x, y),
            textcoords="offset points",
            xytext=(tx, ty),
            arrowprops={
                "width": 1,
                "headwidth": 4,
                "headlength": 5,
                "facecolor": "black"
            },
            fontproperties=font
        )

    # ddda_index = len(df)-1
    # ddda_x = df.loc[ddda_index, "Dim1"]
    # ddda_y = df.loc[ddda_index, "Dim2"]
    # g.annotate(
    #     text="DddA",
    #     xy=(ddda_x, ddda_y),
    #     # textcoords="offset points",
    #     # xytext=(15, 15),
    #     # arrowprops={
    #     #     "width": 1,
    #     #     "headwidth": 4,
    #     #     "headlength": 5,
    #     #     "facecolor": "black"
    #     # },
    #     fontproperties=font
    # )

    handles, labels = g.get_legend_handles_labels()
    legends = g.legend(handles=handles[:6], labels=labels[:6], frameon=False).get_texts()
    for leg in legends:
        leg.set_fontproperties(font)
        # leg.set_size(15)

    plt.savefig(args.out, bbox_inches='tight')

    