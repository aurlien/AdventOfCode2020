from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)    
    next(b, None)
    return zip(a, b)

with open("input.txt") as f:
    numbers =  sorted(map(int, f.readlines()))
    adapters = [0] + numbers + [numbers[-1] + 3]

    pair_diff = list(map(lambda p: p[1]-p[0], pairwise(adapters)))

    one_jolt = len(list(filter(lambda d: d==1, pair_diff)))
    three_jolt = len(list(filter(lambda d: d==3, pair_diff)))

    result = one_jolt * three_jolt

    print(result)
