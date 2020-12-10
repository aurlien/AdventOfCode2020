import re

def parse_rules(rule):
    parts = re.findall(r"((\d+)? ?([a-z]+ [a-z]+)) bag[s]?", rule)

    color = parts[0][0]
    contains = {color: int(num) for _, num, color in parts[1:] if color != 'no other'}
    
    return color, contains

def expand(color, mapping):
    contains = mapping[color]

    bags = 0
    for color in contains:
        count = contains[color]
        bags += count + expand(color, mapping) * count

    return bags

with open("input.txt") as f:
    lines = f.readlines()
    mapping = {k:v for (k,v) in map(parse_rules, lines)} | {'no other': {}}

    print(expand('shiny gold', mapping))
