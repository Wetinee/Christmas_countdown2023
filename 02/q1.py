import re

def max_cubes(line, id):
    cubes = re.findall(r'(\d+) (\w+)', line)
    for n, c in [(12, 'red'), (13, 'green'), (14, 'blue')]:
        if max(int(count) for count, color in cubes if color == c) > n:
            return 0
    return id