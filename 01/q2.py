def compute_value(line):
    first, last = None, None
    for i, c in enumerate(line):
        if c.isdigit():
            first, last = first or int(c), int(c)
        for d, w in enumerate(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")):
            if line[i: i + len(w)] == w:
                first, last = first or d+1, d+1
    return 10*first + last
