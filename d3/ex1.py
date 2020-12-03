def get(x, y, _map):
    width = len(_map[0])
    return _map[x][y % width]

with open("input.txt") as f:
    _map = [line.strip() for line in f.readlines()]
    
    col = 0
    trees = 0
    for row in range(len(_map)):
        if get(row, col, _map) == '#':
            trees += 1
        col += 3
    
    print(trees)


