import re

def parse_input(filename):
    with open(filename) as f:
        parts = f.read().split("\n\n")
        
        rules = re.findall(r"([0-9]+)\-([0-9]+)", parts[0])
        ranges = [range(int(a), int(b)+1) for (a, b) in rules]

        tickets = [list(map(int, line.strip().split(","))) for line in parts[2].split("\n")[1:]]

        return tickets, ranges

def find_invalid_numbers(tickets, ranges):
    numbers = [n for ticket in tickets for n in ticket]

    return list(filter(lambda n: not any(filter(lambda r: n in r, ranges)), numbers))


def main(filename):
    tickets, ranges = parse_input(filename)
    invalid_numbers = find_invalid_numbers(tickets, ranges)

    return sum(invalid_numbers)
            

assert main("test.txt") == 71
result = main("input.txt")
print(result)