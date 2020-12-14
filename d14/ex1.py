MASK = 'mask'
MEM = 'mem'

WILDCARD = 'X'

def print_bitmask(bm):
    print(format(bm, '032b'))

def parse_mask(bit_str):
    zeros = int(''.join('0' if bit == '0' else '1' for bit in bit_str), base=2)
    ones = int(''.join('1' if bit == '1' else '0' for bit in bit_str), base=2)

    return zeros, ones

def parse_input(filename):
    def parse_instruction(s):
        instr, val = s.strip().split(" = ")

        if instr == MASK:
            return MASK, *parse_mask(val)
        else:
            address = int(instr.split("[")[1][:-1])
            return MEM, address, int(bin(int(val)), base=2)

    with open(filename) as f:
        return [parse_instruction(line) for line in f.readlines()]

def main(filename):
    memory = {}
    instructions = parse_input(filename)
    zero_mask = one_mask = 0b0
    for instr, a, b in instructions:
        if instr == MASK:
            zero_mask, one_mask = a, b
        elif instr ==  MEM:
            addr, value = a, b

            value = value & zero_mask | one_mask
            memory[addr] = value

    return sum(memory.values())

if __name__ == "__main__":
    assert main("test1.txt") == 165
    print(main("input.txt"))
