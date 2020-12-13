def parse_input(filename):
    with open(filename) as f:
        timestamp = int(f.readline())
        ids = [int(s) for s in f.readline().split(",") if s != 'x']
        return timestamp, sorted(ids)


def main():
    ts, ids = parse_input("input.txt")

    waiting_times = [(bid, bid - ts % bid) for bid in ids]

    bus_id, must_wait = sorted(waiting_times, key=lambda x: x[1])[0]
    return bus_id * must_wait
    

if __name__ == "__main__":
    result = main()
    print(result)