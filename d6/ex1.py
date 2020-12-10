with open("input.txt") as f:
    lines = [l.replace("\n", "") for l in f.read().split("\n\n")]
    sizes = map(lambda l: len(set(l)), lines)

    print(sum(sizes))   