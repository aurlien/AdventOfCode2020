FLOOR = '.'
SEAT_EMPTY = 'L'
SEAT_OCCUPIED = '#'

def parse_input(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f.readlines()]

def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()

def adjacent(row, col, grid):
    ROW_MAX = len(grid) - 1
    COL_MAX = len(grid[0]) - 1

    up = grid[row - 1][col] if 0 < row else None
    down = grid[row + 1][col] if row < ROW_MAX else None
    left = grid[row][col - 1] if 0 < col else None
    right = grid[row][col + 1] if col < COL_MAX else None
    up_left = grid[row - 1][col - 1] if (0 < row) and (0 < col) else None
    up_right = grid[row - 1][col + 1] if (0 < row) and (col < COL_MAX) else None
    down_left = grid[row + 1][col - 1] if (row < ROW_MAX) and (0 < col) else None
    down_right = grid[row + 1][col + 1] if (row < ROW_MAX) and (col < COL_MAX) else None

    return list(filter(lambda x: x != None and x != FLOOR, [up, down, left, right, up_left, up_right, down_left, down_right]))

def all_empty(adjacent):
    return all(map(lambda x: x == SEAT_EMPTY, adjacent))

def at_least_four_occupied(adjacent):
    return len(list(filter(lambda x: x == SEAT_OCCUPIED, adjacent))) >= 4

def model_round(grid):
    new_grid = []

    for r, row in enumerate(grid):
        new_row = []
        for c, seat in enumerate(row):
            if seat == FLOOR:
                new_row.append(FLOOR)
            else:
                a = adjacent(r, c, grid)
                if seat == SEAT_EMPTY and all_empty(a):
                    new_row.append(SEAT_OCCUPIED)
                elif seat == SEAT_OCCUPIED and at_least_four_occupied(a):
                    new_row.append(SEAT_EMPTY)
                else:
                    new_row.append(seat)

        new_grid.append(new_row)
        new_row = []

    return new_grid

def count_occupied(grid):
    return sum([sum([True for seat in row if seat == SEAT_OCCUPIED]) for row in grid])

def run_model(grid):
    next_grid = model_round(grid)

    if next_grid == grid:
        return grid
    
    return run_model(next_grid)


def main():
    grid = parse_input("input.txt")
    
    stable_grid = run_model(grid)
    return count_occupied(stable_grid)


result = main()
print(result)