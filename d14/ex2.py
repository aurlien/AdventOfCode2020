import re
from more_itertools import powerset
import functools
import operator

MASK = "mask"
MEM = "mem"

def parse_input(filename):
    pattern = r'\[|\]? = '
    with open(filename) as f:
        return [re.split(pattern, line.strip()) for line in f.readlines()]

def print_bitmap(x, message=""):
    print(message + ":\t", format(x, '032b'), "(", x, ")")


def expand_wildcards(addr, mask):
    clear_x_bitmap = int(''.join('0' if bit == 'X' else '1' for bit in mask), base=2)
    addr &= clear_x_bitmap   

    locations =  [i for (i, bit) in enumerate(reversed(mask)) if bit == "X"]
    bits = list(map(lambda x: 1 << x, locations))
    combinations = filter(lambda x: len(x) > 0, powerset(bits))

    wildcard_bitmaps = [functools.reduce(operator.or_, c) for c in combinations] + [0b0]

    return [addr | bitmap for bitmap in wildcard_bitmaps]


def decode_address(addr, mask):
    ones = int(''.join('1' if bit == '1' else '0' for bit in mask), base=2)
    addr |= ones

    return expand_wildcards(addr, mask)


def main(filename):
    memory = {}
    bitmask = 0b0
    for instr in parse_input(filename):
        opcode = instr[0]
        if opcode == MASK:
            bitmask = instr[1]
            
        elif opcode == MEM:
            addr, val = int(instr[1]), int(instr[2])
            for a in decode_address(addr, bitmask):
                memory[a] = val

    return sum(memory.values())

if __name__ == "__main__":
    assert main("test2.txt") == 208
    print(main("input.txt"))