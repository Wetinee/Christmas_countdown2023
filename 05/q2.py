inputs = [int(x) for x in data[0].replace("seeds: ", "").split(" ")]
seeds = [(inputs[i], inputs[i] + inputs[i + 1]) for i in range(0, len(inputs), 2)]

# [[dest_start, source_start, range_len], ...]
maps = [[[int(y) for y in x.split(" ")] for x in data[i].splitlines()[1::]] for i in range(1, 8)]

def remap(start: int, end: int, new_seeds: list[tuple[int]], m: list[int]) -> None:
    for dest_start, source_start, range_len in m:
        
        overlap_start = max(start, source_start)
        overlap_end = min(end, source_start + range_len)

        # Check overlap
        if overlap_start < overlap_end:
            new_seeds.append((dest_start + (overlap_start - source_start), dest_start + (overlap_end - source_start)))

            if start < overlap_start:
                seeds.append((start, overlap_start))
            if overlap_end < end:
                seeds.append((overlap_end, end))
            break
    else:
        # No overlap
        new_seeds.append((start, end))

def multi_maps(seeds, maps):
    for m in maps:
        new_seeds = []
        while seeds:
            start, end = seeds.pop()
            remap(start, end, new_seeds, m)
        seeds = new_seeds
    return min(seeds)[0]
