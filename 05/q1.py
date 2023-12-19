def map_seeds(data):
    seeds = [int(n) for n in data[0].split(":")[1][1:].split(" ")]
    maps, rules, tmp, result = [], [], [], []

    for line in data[2:]:
        if not line: 
            continue
        if line[0].isdigit():
            line = [int(n) for n in line.split(" ")]
            tmp.append([(line[0],line[0]+line[2]-1), (line[1], line[1]+line[2]-1)])
        else:
            maps.append(line.split(":")[0])
            if tmp: 
                rules.append(tmp)
                tmp = []
    rules.append(tmp)

    for s in seeds:
        for r in rules:
            for interval in r:
                if interval[1][0] <= s <= interval[1][1]:
                    s = s - interval[1][0] + interval[0][0]
                    break
        result.append(s)

    return min(result)