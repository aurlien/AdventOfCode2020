def count_group(group):
    group = map(lambda g: set(g), group)
    common = set.intersection(*group)
    return len(common)

with open("input.txt") as f:
    lines = [l.split("\n") for l in f.read().split("\n\n")]
    print(sum([count_group(l) for l in lines]))