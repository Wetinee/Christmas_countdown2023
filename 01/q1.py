def compute_value(line):
    first, last = None, None
    for c in line:
        if c.isdigit():
            first, last = first or int(c), int(c)
    return first*10 + last

