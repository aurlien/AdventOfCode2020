
def parse_input(lines):
    return [line.strip().split(': ') for line in lines]

def validate_ex1(password, policy):
    limits, char = policy.split(' ')
    low, high = tuple(map(int, limits.split('-')))
    count = password.count(char)

    return low <= count <= high

def ex1(lines):
    valid_passwords = [password for (policy, password) in lines if validate_ex1(password, policy)]

    return len(valid_passwords)

def validate_ex2(password, policy):
    rule, char = policy.split(' ')
    positions = map(int, rule.split('-'))

    matches = filter(lambda p: password[p-1] == char, positions)

    return len(matches) == 1


def ex2(lines):
    valid_passwords = [password for (policy, password) in lines if validate_ex2(password, policy)]

    return len(valid_passwords)


def test():
    lines = [
        ('1-3 a', 'abcde'),
        ('1-3 b', 'cdefg'),
        ('2-9 c', 'ccccccccc')
    ]

    assert ex1(lines) == 2
    assert ex2(lines) == 1
    

if __name__ == "__main__":
    test()

    with open("input.txt") as f:
        parsed = parse_input(f)

        print(ex1(parsed))
        print(ex2(parsed))


