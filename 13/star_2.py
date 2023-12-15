def get_patterns():
    D = open("input.txt").read().strip()
    lines = D.split("\n\n")
    patterns = []

    for pattern in lines:
        rows = pattern.split("\n")
        l = [list(x) for x in rows]
        patterns.append(l)
    return patterns


def check_mask_symmetry(mask):
    for i in range(len(mask) - 1, -1, -1):
        sub_mask = mask[: i + 1]
        if sub_mask == sub_mask[::-1] and len(sub_mask) != 1 and len(sub_mask) % 2 == 0:
            return True
    return False


def get_mask(pattern, map):
    mask = []
    for p in pattern:
        mask.append(map["".join(p)])
    return mask


def create_map(pattern):
    map = {}
    for p in pattern:
        p = "".join(p)
        map[p] = map.get(p, len(map))
    return map


def map_symmetry(pattern):
    map = create_map(pattern)
    mask = get_mask(pattern, map)
    sym = check_mask_symmetry(mask)
    if not sym:
        sym = check_mask_symmetry(mask[::-1])

    return sym


def get_contiguous_symmetry(pattern):
    map = create_map(pattern)
    mask = get_mask(pattern, map)
    sym = check_mask_symmetry(mask)

    if not sym:
        mask = mask[::-1]
    for i in range(len(mask) - 1, -1, -1):
        sub_mask = mask[: i + 1]
        if sub_mask == sub_mask[::-1] and len(sub_mask) != 1 and len(sub_mask) % 2 == 0:
            return sub_mask

    return []

def get_contiguous_symmetry_2(pattern, contig):
    map = create_map(pattern)
    mask = get_mask(pattern, map)
    sym = False
    
    for i in range(len(mask) - 1, -1, -1):
        sub_mask = mask[: i + 1]
        if sub_mask == sub_mask[::-1] and len(sub_mask) != 1 and len(sub_mask) % 2 == 0:
            if contig != sub_mask:
                sym = True
    if not sym:
        mask = mask[::-1]
    for i in range(len(mask) - 1, -1, -1):
        sub_mask = mask[: i + 1]
        if sub_mask == sub_mask[::-1] and len(sub_mask) != 1 and len(sub_mask) % 2 == 0:
            return sub_mask
    return []


def print_pattern(pattern):
    print("")
    for p in pattern:
        print("".join(p))
    print("")


def find_other_symmetry(pattern, position, transposed, og_contig):
    print("symetry at", position, "and transposed is", transposed)
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            temp_map = pattern
            temp_map[i][j] = "." if temp_map[i][j] == "#" else "#"
            
            sym = map_symmetry(temp_map)
            map = create_map(temp_map)
            mask = get_mask(temp_map, map)
            contig = get_contiguous_symmetry_2(temp_map, og_contig)
            sym_pos = find_sym_position(mask, contig)
            
            if sym: 
                a=1
                print(f"""Symetry found in intial. The new symetry pos = {sym_pos} and the old pos = {position}.\nContiguous = {contig} and the mask is {mask}""")

            if sym and (not sym_pos == position or transposed) and contig!=[]:
                print_pattern(temp_map)
                print(f"""Symetry found in intial. The new symetry pos = {sym_pos} and the old pos = {position}.\nContiguous = {contig} and the mask is {mask}""")
                return temp_map, False
            else:
                reversed_map = [list(row)[::-1] for row in zip(*temp_map)]

                t_sym = map_symmetry(reversed_map)
                map = create_map(reversed_map)
                mask = get_mask(reversed_map, map)
                contig = get_contiguous_symmetry_2(reversed_map, og_contig)
                sym_pos = find_sym_position(mask, contig)   

                if t_sym: 
                    a=1
                    #print(f"""Symetry found in transpose. Sym Pos = {sym_pos} and Pos = {position}.\nContiguous = {contig} and the mask is {mask}""")   
   
                if t_sym and (not sym_pos == position or not transposed) and contig != []:
                    print_pattern(reversed_map) 
                    print(f"""Symetry found in transpose. Sym Pos = {sym_pos} and Pos = {position}.\nContiguous = {contig} and the mask is {mask}""")   
                    return reversed_map, True
            temp_map[i][j] = "." if temp_map[i][j] == "#" else "#"
            
    return None, False


def find_sym_position(mask, contig):
    for i in range(len(mask) - len(contig) + 1):
       if mask[i:i+len(contig)] == contig:
           return i + (len(contig)//2)
    return -1


def loop_pattern(pattern):
    smudge_pattern = pattern
    transposed = False
    is_symmetrical = map_symmetry(pattern)
    if not is_symmetrical:
        transposed = True
        pattern = [list(row)[::-1] for row in zip(*pattern)]

    map = create_map(pattern)
    mask = get_mask(pattern, map)
    contig = get_contiguous_symmetry(pattern)
    print(mask, contig)
    position = find_sym_position(mask, contig)
    print(position)

    new_pattern, new_transposed = find_other_symmetry(
        smudge_pattern, position, transposed, contig
    ) 

    assert new_pattern != None, "New pattern was not found"

    new_map = create_map(new_pattern)
    new_mask = get_mask(new_pattern, new_map)
    new_contig = get_contiguous_symmetry(new_pattern)

    val = len(new_contig) // 2
    for i in range(len(new_mask) - len(new_contig) + 1):
        if new_mask[i : i + len(new_contig)] == new_contig:
            val += i
            break

    return val * 100 if not new_transposed else val


def main():
    pattern = get_patterns()
    symetries = 0

    for i, pattern in enumerate(pattern):
        print("\n--------- AT POSITION",i,"---------\n")
        print_pattern(pattern)
        symetries += loop_pattern(pattern)
  
    print(symetries)


if __name__ == "__main__":
    main()
