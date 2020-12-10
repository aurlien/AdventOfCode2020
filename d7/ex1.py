import re

def parse_rules(rule):
    parts = re.findall("([a-z]+ [a-z]+) bag[s]?", rule)

    color = parts[0]
    contains = set(parts[1:])
    
    return color, contains

def expand(color, mapping):
    colors = set()
    for color in mapping[color]:
        colors.add(color)
        colors = colors | expand(color, mapping)
    return colors

with open("input.txt") as f:
    lines = f.readlines()
    mapping = {k:v for (k,v) in map(parse_rules, lines)} | {'no other': {}}

    expanded = map(lambda color: expand(color, mapping), mapping.keys())

    matches = filter(lambda x: 'shiny gold' in x, expanded)

    print(len(list(matches)))

