import math

FORWARD = 'F'
LEFT = 'L'
RIGHT = 'R'
NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'

def parse_instruction(s):
    action = s[0]
    value = int(s[1:])

    return action, value

def left(degrees, dx, dy):
    times = degrees // 90
    if times == 0:
        return (dx, dy)
    return left(degrees-90, dx=-dy, dy=dx)

def right(degrees, dx, dy):
    times = degrees // 90
    if times == 0:
        return (dx, dy)
    return right(degrees-90, dx=dy, dy=-dx)

def manhattan_distance(x, y):
    return abs(x) + abs(y)

def next_step(position, direction, instruction):
    action, value = instruction

    x, y = position
    dx, dy = direction

    if action == FORWARD:
        x += dx * value
        y += dy * value
    elif action == NORTH:
        y += value
    elif action == SOUTH:
        y -= value
    elif action == EAST:
        x += value
    elif action == WEST:
        x -= value
    elif action == LEFT:
        dx, dy = left(value, dx, dy)
    elif action == RIGHT:
        dx, dy = right(value, dx, dy)
        
    return (x, y), (dx, dy)

def run(instructions):
    position = (0, 0)
    direction = (1, 0)

    for instruction in instructions:
        position, direction = next_step(position, direction, instruction)

    return manhattan_distance(*position)

with open("input.txt") as f:
    instructions = map(parse_instruction, f.readlines())
    position = run(instructions)
    print(position)