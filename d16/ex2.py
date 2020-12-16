import re

def parse_input(filename):
    with open(filename) as f:
        parts = f.read().split("\n\n")
        
        matches = re.findall(r"([a-z ]+): ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)", parts[0])
        rules = {name: [range(int(a0), int(a1)+1), range(int(b0), int(b1)+1)] for (name, a0, a1, b0, b1) in matches}

        my_ticket = list(map(int, parts[1].split("\n")[1].split(",")))

        tickets = [list(map(int, line.strip().split(","))) for line in parts[2].split("\n")[1:]]

        return my_ticket, tickets, rules

def is_valid(ticket, rules):
    ranges = [r for value in rules.values() for r in value]
    return all(map(lambda t: any(map(lambda r: t in r, ranges)), ticket))

def solve_positions(matches):
    if len(matches) == 0:
        return {}

    s = { k: v[0] for (k, v) in matches.items() if len(v) == 1}

    for k in s.keys():
        del matches[k]

    for key, value in matches.items():
        matches[key] = [v for v in value if v not in s.values()]

    return s | solve_positions(matches)


def main(filename):
    my_ticket, tickets, rules = parse_input(filename)
    
    valid_tickets = [t for t in tickets if is_valid(t, rules)] + [my_ticket]
    ticket_length = len(valid_tickets[0])
    
    matches = {}

    for name, ranges in rules.items():
        m = []
        for i in range(ticket_length):
            if all([any(map(lambda r: t[i] in r, ranges)) for t in valid_tickets]):
                m.append(i)
        matches[name] = m
    
    positions = solve_positions(matches)
    res = 1
    for s, i in positions.items():
        if "departure" in s:
            res *= my_ticket[i]
    return res


result = main("input.txt")
print(result)