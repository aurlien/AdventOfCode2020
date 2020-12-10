from itertools import groupby
from math import prod

def find_consecutive_numbers(iterable):
    return [list(map(lambda x: x[1], g)) for k, g in groupby(enumerate(adapters), lambda x: x[1]-x[0])]

def combinations(n_consecutive):
    default = 1
    return {
        3: 2, # 2^1
        4: 4, # 2^2
        5: 7  # 2^3-1
    }.get(n_consecutive, default)

with open("input.txt") as f:
    adapters =  [0] + sorted(map(int, f.readlines()))
    consecutive = find_consecutive_numbers(adapters)

    counts = map(len, consecutive)
    combinations = map(combinations, counts)
    result = prod(combinations)

    print(result)
    
