import time
D = open("input.txt").read().strip()
lines = D.split("\n")

categories = D.split("\n\n")
seed_input = categories.pop(0).split(":")[1].strip().split(" ")
seed_input = [int(seed) for seed in seed_input]

counter = 0
pair = []
seed_pairs = []
for seed in seed_input:
    pair.append(seed)
    if len(pair) == 2:
        seed_pairs.append(pair)
        pair = []


def loop_map(r, map, seed):
    dest_start = int(r[0])
    source_start = int(r[1])
    range_len = int(r[2])

    if seed == source_start:
        map[seed] = seed + (dest_start - source_start)
    elif seed > source_start and seed < source_start + range_len:
        map[seed] = seed + (dest_start - source_start)

    return map

lows = []
seeds = []
for start, count in seed_pairs:
    seeds = list(range(start, start + count))

    for conv in categories:
        cat_nums = conv.split("\n")
        cat_nums.pop(0)

        map = {}
        for i in range(len(seeds)):
            for row in cat_nums:
                r = row.split(" ")
                map = loop_map(r, map, seeds[i])

        for i in range(len(seeds)):
            seeds[i] = map[seeds[i]] if seeds[i] in map else seeds[i]
    
    lows.append(min(seeds))
print(min(lows))
