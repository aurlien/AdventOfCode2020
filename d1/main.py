from itertools import combinations

def parse_input(f):
    return [int(n) for n in f]

def sum_to(n, *args):
    return sum(args) == n

def ex1(ns):
    pairs = combinations(ns, 2)
    return next(a * b for (a, b) in pairs if sum_to(2020, a, b)) 

def ex2(ns):
    triples = combinations(ns, 3)
    return next(a * b * c for (a, b, c) in triples if sum_to(2020, a, b, c))

def test():
    expences = [1721, 979, 366, 299, 675, 1456]

    assert ex1(expences) == 514579 # 1721 * 299
    assert ex2(expences) == 241861950 # 979 * 366 * 675
    

if __name__ == "__main__":
    test()

    f = open("input.txt")
    numbers = parse_input(f)

    print(ex1(numbers))
    print(ex2(numbers))



