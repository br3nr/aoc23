from typing import List


def extract_gears(part_coords: List[int], grid: List[List[int]]):
    gears = []
    for part in part_coords:
        part_num = grid[part[0]][part[1]]
        found_left, found_right = False, False
        l_c, r_c = -1, 1
        while not found_left:
            c = part[1]
            if grid[part[0]][part[1] + l_c].isdigit():
                part_num = grid[part[0]][c + l_c] + part_num
                l_c = l_c - 1
            else:
                found_left = True
        while not found_right:
            c = part[1]
            if grid[part[0]][c + r_c].isdigit():
                part_num = part_num + grid[part[0]][c + r_c]
                r_c = r_c + 1
            else:
                found_right = True
        gears.append(int(part_num))
    return gears


def gear_search(i: int, j: int, grid: List[List[str]]) -> int:
    part_coords = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            if grid[i + y][j + x].isdigit():
                part_coords.append([i + y, j + x])

    return part_coords


def remove_duplicate_parts(part_coords):
    new_part_coords = [part_coords[0]]
    for i in range(1, len(part_coords)):
        cur_i, cur_j = part_coords[i - 1][0], part_coords[i - 1][1]
        next_i, next_j = part_coords[i][0], part_coords[i][1]

        if cur_i == next_i and next_j - cur_j == 1:
            continue
        new_part_coords.append(part_coords[i])
    return new_part_coords


def calc_gear_rat(gears):
    # calculate the gear ratio
    ratio = 0
    if len(gears) > 1:
        ratio = 1
        for gear in gears:
            ratio *= gear
    return ratio


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        specials = "*"
        coords = []
        sums = 0

        file_iter = file.readlines()
        grid = [[] for _ in range(len(file_iter))]
        for i, sequence in enumerate(file_iter):
            for j, char in enumerate(sequence):
                grid[i].append(char)
                if char in specials:
                    coords.append([i, j])

        ratios = 0
        for coord in coords:
            part_coords = gear_search(coord[0], coord[1], grid)
            part_coords = remove_duplicate_parts(part_coords)
            gears = extract_gears(part_coords, grid)
            ratios += calc_gear_rat(gears)
        print(ratios)
