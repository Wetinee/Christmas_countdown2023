import re

def sum_scratchcards(data):
    data = [[a, [int(n) for n in b.split()], [int(n) for n in c.split()]]for a, b, c in [re.split(r'[:|]', line) for line in data]]
    scratchcards = [1 for _ in range(len(data))]
    match_numbers = [len([n for n in b if n in c]) for _, b, c in data]
    pairs = list(zip(scratchcards, match_numbers))
    for i, (s, m) in enumerate(pairs):
        for next in range(1, m+1):
            if (i+next) < len(pairs):
                pairs[i+next] = (pairs[i+next][0] + s, pairs[i+next][1])
    return sum(s for s, _ in pairs)
        
