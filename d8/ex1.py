
def parse_instruction(line): 
    parts = line.split()
    return parts[0], int(parts[1])

def parse_input(lines):
    return list(map(parse_instruction, lines))

def execute(instructions, acc, ins, seen):
    if ins in seen:
        return acc

    seen.add(ins)
    op, val = instructions[ins]

    if op == "jmp":
        return execute(instructions, acc, ins + val, seen)
    elif op == "acc":
        return execute(instructions, acc + val, ins + 1, seen)
    elif op == "nop":
        return execute(instructions, acc, ins + 1, seen)

with open("input.txt") as f:
    lines = f.readlines()
    instructions = parse_input(lines)

    result = execute(instructions, 0, 0, set())
    print(result)

