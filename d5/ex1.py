
def parse_ticket(ticket):
    ticket = ticket \
        .replace('F', '0') \
        .replace('B', '1') \
        .replace('L', '0') \
        .replace('R', '1') \

    row = int(ticket[:7], base=2)
    col = int(ticket[7:], base=2)

    return row, col, row * 8 + col

def test():
    # (ticket, (row, col, ID))
    test_cases = [ 
        ("FBFBBFFRLR", (44, 5, 357)),
        ("BFFFBBFRRR", (70, 7, 567)),
        ("FFFBBBFRRR", (14, 7, 119)),
        ("BBFFBBFRLL", (102, 4, 820))
    ]

    for (ticket, expected) in test_cases:
        assert parse_ticket(ticket) == expected

test()

with open("input.txt") as f:
    lines = f.readlines()
    tickets = map(parse_ticket, lines)
    ids = map(lambda seq: seq[-1], tickets)

    print(max(ids))
    
