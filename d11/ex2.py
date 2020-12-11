FLOOR = '.'
SEAT_EMPTY = 'L'
SEAT_OCCUPIED = '#'

UP    = -1
DOWN  = +1
RIGHT = +1
LEFT  = -1

def parse_input(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f.readlines()]

def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()

def adjacent(row, col, grid):
    ROW_MAX = len(grid) 
    COL_MAX = len(grid[0])

    def next(row, col, dx=0, dy=0):
        x = row + dx
        y = col + dy

        seat = grid[x][y] if (0 <= x < ROW_MAX) and (0 <= y < COL_MAX) else None
      
        if seat == FLOOR:
            seat = next(row + dx, col + dy, dx, dy)
        
        return seat

    right = lambda row, col: next(row, col, dy=RIGHT)
    left = lambda row, col: next(row, col, dy=LEFT)
    up = lambda row, col: next(row, col, dx=UP)
    down = lambda row, col: next(row, col, dx=DOWN)
    up_left = lambda row, col: next(row, col, dx=UP, dy=LEFT)
    down_left = lambda row, col: next(row, col, dx=DOWN, dy=LEFT)
    up_right = lambda row, col: next(row, col, dx=UP, dy=RIGHT)
    down_right = lambda row, col: next(row, col, dx=DOWN, dy=RIGHT)

    seats = [fun(row, col) for fun in [up, down, left, right, up_left, up_right, down_left, down_right]]

    return list(filter(lambda s: s != None and s != FLOOR, seats))

def all_empty(adjacent):
    return all(map(lambda x: x == SEAT_EMPTY, adjacent))

def at_least_five_occupied(adjacent):
    return len(list(filter(lambda x: x == SEAT_OCCUPIED, adjacent))) >= 5

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
                elif seat == SEAT_OCCUPIED and at_least_five_occupied(a):
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

print(main())