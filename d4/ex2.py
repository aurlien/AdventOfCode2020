import re

def between(field, low, high):
    return low <= int(field) <=  high

def valid_height(height):
    value, unit = height[:-2], height[-2:]
    if unit == "cm":
        return between(value, 150, 193)
    elif unit == "in":
        return between(value, 59, 76)
    else:
        return False

required_fields = {
    'byr', #(Birth year)
    'iyr', #(Issue year)
    'eyr', #(Expiration year)
    'hgt', #(Height)
    'hcl', #(Hair Color)
    'ecl', #(Eye Color)
    'pid', #(Passport ID)
}

is_valid = {
    'byr': lambda year: between(year, 1920, 2002), #(Birth year)
    'iyr': lambda year: between(year, 2010, 2020), #(Issue year)
    'eyr': lambda year: between(year, 2020, 2030), #(Expiration year)
    'hgt': lambda height: valid_height(height), #(Height)
    'hcl': lambda hcl: re.match("#[0-9a-f]{6}", hcl), #(Hair Color)
    'ecl': lambda ecl: re.match("amb|blu|brn|gry|grn|hzl|oth", ecl), #(Eye Color)
    'pid': lambda pid: re.match("^[0-9]{9}$", pid), #(Passport ID)
}

def validate(passport):
    fields = [pair.split(":") for pair in passport.split(" ")]
    
    keys = { p[0] for p in fields if p[0] != "cid" }
    if keys != required_fields:
        return False

    return all(is_valid[key](value) for (key, value) in fields if key != "cid")
    

def parse_input(filename):
    with open(filename, "r") as f:
        passports = [line.replace("\n", " ") for line in f.read().split("\n\n")]
        return passports

def run(filename):
    passports = parse_input(filename)
    valid = [validate(passport) for passport in passports]

    return sum(valid)

def test():
    assert is_valid['byr'](2002)
    assert not is_valid['byr'](2003)

    assert is_valid['hgt']('60in')
    assert is_valid['hgt']('190cm')
    assert not is_valid['hgt']('190in')
    assert not is_valid['hgt']('190')

    assert is_valid['hcl']('#123abc')
    assert not is_valid['hcl']('#123abz')
    assert not is_valid['hcl']('123abc')

    assert is_valid['ecl']('brn')
    assert not is_valid['ecl']('wat')

    assert is_valid['pid']('000000001')
    assert not is_valid['pid']('0123456789')

    assert run("test_valid_02.txt") == 4
    assert run("test_invalid_02.txt") == 0

def main():
    test()
    print(run("input.txt"))

if __name__ == "__main__":
    main()

