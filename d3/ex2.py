import math

def get(x, y, _map):
    width = len(_map[0])
    return _map[x][y % width]

def count_trees(slope, _map):
    right, down = slope
    height = len(_map)
    print("right:", right, ", down:", down)

    row, col, trees = 0, 0, 0
    while row < height:
        if get(row, col, _map) == '#':
            trees += 1
        row += down
        col += right
    
    return trees

with open("input.txt") as f:
    _map = [line.strip() for line in f.readlines()]

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    trees = [count_trees(slope, _map) for slope in slopes]

    print(math.prod(trees))


