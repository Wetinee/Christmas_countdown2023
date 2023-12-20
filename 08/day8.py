import math


def parse(data):
    instructions = [int(n) for n in data[0].replace("L", "0").replace("R", "1")]
    mappings = {}
    for line in data[2:]:
        key, value = line.split("=")
        value = value.replace("(", "").replace(")", "").replace(",", "").split()
        mappings[key.strip()] = value
    return [instructions, mappings]


def cnt_steps(data):
    instructions, mappings = parse(data)
    start = "AAA"
    steps = 0

    while start != "ZZZ":
        for d in instructions:
            start = mappings[start][d]
            steps += 1

    return steps


def cnt_steps_q2(data):
    instructions, mappings = parse(data)
    start, steps = [k for k in mappings.keys() if k[-1] == "A"], []

    for s in start:
        cnt = 0
        while not s.endswith("Z"):
            for d in instructions:
                s = mappings[s][d]
                cnt += 1
                if s.endswith("Z"):
                    steps.append(cnt)
        continue

    return math.lcm(*steps)
