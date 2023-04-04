import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--blast", type=str)
    parser.add_argument("--out", type=str)
    args = parser.parse_args()

    lines = open(args.blast, "r").readlines()
    output = []
    for l in lines:
        items = l.strip().split("\t")
        output.append(f"{items[3]}\t{float(items[2])/100}\t{float(items[-1])/100}\n")
    open(args.out, "w").writelines(output)