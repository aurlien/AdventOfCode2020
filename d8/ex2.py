
def parse_instruction(line): 
    parts = line.split()
    return parts[0], int(parts[1])

def parse_input(lines):
    return list(map(parse_instruction, lines))

def fix_instruction(op):
    if op == "jmp":
        return "nop"
    else: 
        return "jmp"

def execute(instructions, acc, ins, seen, changed):
    if ins >= len(instructions):
        return acc

    if ins in seen:
        return -1

    op, val = instructions[ins]

    next_ins = ins
    next_acc = acc
    next_seen = seen | { ins }

    if op == "jmp":
        next_ins += val
    elif op == "acc":
        next_acc += val
        next_ins += 1
    elif op == "nop":
        next_ins += 1


    res = execute(instructions, next_acc, next_ins, next_seen, changed)
    if not changed and op in ("jmp", "nop") and res == -1:
        instructions[ins] = (fix_instruction(op), val)

        return execute(instructions, acc, ins, seen, True)
    else:
        return res
        

with open("input.txt") as f:
    lines = f.readlines()
    instructions = parse_input(lines)

    result = execute(instructions, 0, 0, set(), False)
    print(result)

