from typing import List

specials = "!@#$%^&*()_+=/-"
coords = []
sums = 0

def char_search(i: int, j: int, grid: List[List[str]]) -> bool:
    for y in range(-1, 2, 1):
        for x in range(-1, 2, 1):
            try:
                if grid[i + y][j + x] in specials:
                    return True
            except IndexError:
                pass
    return False

with open("input.txt", "r") as file:
    file_iter = file.readlines()
    grid = [[] for _ in range(len(file_iter))]
    for i, sequence in enumerate(file_iter):
        on_num = False
        for j, char in enumerate(sequence):
            grid[i].append(char)
            if char == "." or char in specials:
                on_num = False
            elif char.isdigit() and not on_num:
                coords.append([i, j])
                on_num = True

for coord in coords:
    i, j = coord[0], coord[1]
    over, found = False, False
    part_num = ""
    counter = 0

    while not over:
        if not found:
            found = char_search(i, j + counter, grid)
        part_num += grid[i][j + counter]
        counter += 1
        if not grid[i][j + counter].isdigit():
            over = True

    if found:
        sums += int(part_num)

print(sums)
