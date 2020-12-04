required_fields = {
    'byr', #(Birth Year)
    'iyr', #(Issue Year)
    'eyr', #(Expiration Year)
    'hgt', #(Height)
    'hcl', #(Hair Color)
    'ecl', #(Eye Color)
    'pid', #(Passport ID)
}

def validate_year(field, low, high):
    return low <= field <=  high

def validate(passport):
    keys = { pair.split(":")[0] for pair in passport.split(" ")} - {'cid', ''}

    return keys == required_fields

def parse_input(filename):
    with open(filename, "r") as f:
        passports = [line.replace("\n", " ") for line in f.read().split("\n\n")]
        return passports

def run(filename):
    passports = parse_input(filename)
    valid = [validate(passport) for passport in passports]

    return sum(valid)

def main():
    assert run("test.txt") == 2
    
    print(run("input.txt"))


if __name__ == "__main__":
    main()