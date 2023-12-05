D = open("input.txt").read().strip()
lines = D.split("\n")

categories = D.split("\n\n")
seeds = categories.pop(0).split(":")[1].strip().split(" ")
seeds = [int(seed) for seed in seeds]


def loop_map(r, map, seed):
    dest_start = int(r[0])
    source_start = int(r[1])
    range_len = int(r[2])

    if seed == source_start:
        map[seed] = seed + (dest_start - source_start)
    elif seed > source_start and seed < source_start + range_len:
        map[seed] = seed + (dest_start - source_start)

    return map


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

print(min(seeds))
