import re

def match_nums(data):
    data = [[a, [int(n) for n in b.split()], [int(n) for n in c.split()]]for a, b, c in [re.split(r'[:|]', line) for line in data]]
    return sum(pow(2,l-1) for l in [len([n for n in line[1] if n in line[2]]) for line in data] if l != 0)