
def get_patterns():
    D = open("input.txt").read().strip()
    lines = D.split("\n\n")
    patterns = []

    for pattern in lines:
        rows = pattern.split("\n")
        l = [list(x) for x in rows]
        patterns.append(l)


def check_mask_symmetry(mask):
    for i in range(len(mask)-1, -1, -1):
        sub_mask = mask[:i+1]
        if sub_mask == sub_mask[::-1] and len(sub_mask) != 1 and len(sub_mask) % 2 == 0:
        
            return True
    return False


def get_mask(pattern, map):
    mask = []
    for p in pattern:
        mask.append(map[''.join(p)])
    return mask


def map_symmetry(pattern):
    map = create_map(pattern)
    mask = get_mask(pattern, map)
    sym = check_mask_symmetry(mask)
    if not sym:
        sym = check_mask_symmetry(mask[::-1])
    
    return sym


def create_map(pattern):
    map = {}
    for p in pattern:
        p = ''.join(p)
        map[p] = map.get(p, len(map))
    return map


def get_contiguous_symmetry(pattern):
    map = create_map(pattern)
    mask = get_mask(pattern, map)
    print(mask)
    sym = check_mask_symmetry(mask)
    if not sym:
        mask = mask[::-1]
    
    for i in range(len(mask)-1, -1, -1):
        sub_mask = mask[:i+1] 
        print(sub_mask)
        if sub_mask == sub_mask[::-1] and len(sub_mask) != 1 and len(sub_mask) % 2 == 0:
            return sub_mask
    

def loop_pattern(pattern):
    for line in pattern:
        print(''.join(line))

    transposed = False
    if not map_symmetry(pattern):
        transposed = True
        pattern = [list(row)[::-1] for row in zip(*pattern)]

    map = create_map(pattern)
    mask = []
    for p in pattern:
        mask.append(map[''.join(p)])
   
    contig = get_contiguous_symmetry(pattern) 

    val = len(contig)//2
    for i in range(len(mask) - len(contig) + 1):
        if mask[i:i + len(contig)] == contig:
            val += i
            break

    return val * 100 if not transposed else val


def main():
    pattern = get_patterns()
    symetries = 0
    
    for i,pattern in enumerate(patterns):
        symetries += loop_pattern(pattern)

    print(symetries)


if __name__ == "__main__":
    main()

