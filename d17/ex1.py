from itertools import product
from collections import defaultdict

ACTIVE = '#'
INACTIVE = '.'

get_x = lambda triple: triple[0]
get_y = lambda triple: triple[1]
get_z = lambda triple: triple[2]

def print_state(active_set):
    max_x = get_x(max(active_set, key=get_x))
    min_x = get_x(min(active_set, key=get_x))

    max_y = get_y(max(active_set, key=get_y))
    min_y = get_y(min(active_set, key=get_y))

    max_z = get_z(max(active_set, key=get_z))
    min_z = get_z(min(active_set, key=get_z))

    print()
    print(active_set)
    print("x:", min_x, max_x)
    print("y:", min_y, max_y)
    print("z:", min_z, max_z)

    for z in range(min_z, max_z+1):
        print()
        print("z =", z)
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                v = ACTIVE if (x, y, z) in active_set else INACTIVE
                print(v, end="")
            print()
        print()


def parse_input(filename):
    with open(filename) as f:
        states = [list(l.strip()) for l in f.readlines()]

        active = set()
        for x, line in enumerate(states):
            for y, val in enumerate(line):
                if val == ACTIVE:
                    active.add((x, y, 0))

        return active

def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]

def get_neighbours(diff=1):
    r = range(-diff, diff+1)
    return [(x,y,z) for x in r for y in r for z in r if not x == y == z == 0]

def next_round(active_state):
    neighbours = get_neighbours()
    active_neighbours = defaultdict(int)

    for active in active_state:
        for n in neighbours:
            neighbour = add(active, n)
            active_neighbours[neighbour] += 1
    
    next_active = set()
    for active in active_state:
        if active_neighbours[active] in (2,3):
            next_active.add(active)

    for n, count in active_neighbours.items():
        if count == 3:
            next_active.add(n)

    return next_active

def count_active(state):
    return 

state = parse_input("input.txt")
for round in range(6):
    state = next_round(state)
    print_state(state)

print(len(state))
