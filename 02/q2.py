import re

def max_cubes(line):
    cubes = re.findall(r'(\d+) (\w+)', line)
    result = 1
    for c in ['red', 'green', 'blue']:
        result *= max(int(cnt) for cnt, color in cubes if color == c)
    return result