import re
from functools import reduce

def run_further(data):

    lines = [[int(x) for x in re.split(r'[:\s]', line) if x.isdigit()] for line in data]
    time_distance_pairs = list(zip(lines[0], lines[1]))   # [(time1, distance1), (time2, distance2), ...]

    return reduce(lambda x, y: x* y, [len([i for i in range(time+1) if i*(time-i) > distance]) for time, distance in time_distance_pairs])
    
