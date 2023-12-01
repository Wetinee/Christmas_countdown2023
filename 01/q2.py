def compute_value(line):
    first, last = None, None
    for i, c in enumerate(line):
        if c.isdigit():
            first, last = first or int(c), int(c)
        for d, w in enumerate(("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")):
            if line[i: i + len(w)] == w:
                first, last = first or d, d
    return first*10 + last
