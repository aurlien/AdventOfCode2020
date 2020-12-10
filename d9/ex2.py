from itertools import takewhile

def find_contigous(numbers, result):
    seq_sum = 0
    sequence = []
    for i in numbers:
        seq_sum += i
        sequence.append(i)

        if seq_sum == result:
            return sequence
        elif seq_sum > result:
            return find_contigous(numbers[1:], result)
    

with open("input.txt") as f:
    numbers = [int(i) for i in f.readlines()]
    
    result = 144381670
    seq = find_contigous(numbers, result)

    print(max(seq) + min(seq))

