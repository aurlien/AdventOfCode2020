import math

def parse_input(filename):
    with open(filename) as f:
        f.readline() # first line is not relevant
        return [(i, int(s)) for i, s in enumerate(f.readline().split(",")) if s != 'x']
        

def congruence_equation(i, bus_id):
    # form: x ≡ a (mod n)
    return (bus_id - i) % bus_id, bus_id


def solve(system):
    # system: [(m1, a1), (m2, a2), ..., (mr, ar)]
    # M := m1 * m2 * ... * mr
    # Mi := M / mi
    # ki := inverse to Mi modulo mi ==> ki * Mi ≡ 1 (mod mi)
    # x ≡ sum(ai * Mi * ki) (mod M)

    M = math.prod([mi for (ai, mi) in system])

    def part(ai, mi):
        Mi = M // mi
        ki = pow(M // mi, -1, mi)
        return ai * Mi * ki

    return sum(part(*s) for s in system) % M
    

def main():
    busses = parse_input("input.txt")
    system = [congruence_equation(i, bus_id) for (i, bus_id) in busses]

    return solve(system)


if __name__ == "__main__":
    result = main()
    print(result)