from itertools import permutations

def validate(numbers, preamble_length):
    preamble = numbers[:preamble_length]
    number = numbers[preamble_length]

    pairs = permutations(preamble, 2)
    pair_sums = set([a+b for (a, b) in pairs])

    if number not in pair_sums:
        return number
    
    return validate(numbers[1:], preamble_length)



with open("input.txt") as f:
    numbers = [int(i) for i in f.readlines()]
    
    print(validate(numbers, 25))

