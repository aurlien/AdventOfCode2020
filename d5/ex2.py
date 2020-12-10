def parse_ticket(ticket):
    ticket = ticket \
        .replace('F', '0') \
        .replace('B', '1') \
        .replace('L', '0') \
        .replace('R', '1') \

    row = int(ticket[:7], base=2)
    col = int(ticket[7:], base=2)

    return row, col, row * 8 + col

def main(lines):
    tickets = sorted(map(parse_ticket, lines))
    candidates = list(map(lambda x: x[2], tickets))

    # skip first and last
    candidates.pop(0)
    candidates.pop()

    for i, id in enumerate(candidates):
        if id + 2 == candidates[i+1]:
            return id + 1

    
with open("input.txt") as f:
    lines = f.readlines()
    result = main(lines)

    print(result)