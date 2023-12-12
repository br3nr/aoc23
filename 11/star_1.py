def cosmically_inflate(arr):
    space = []
    for line in arr:
        if len(set(line)) == 1:
            space.append(line)
        space.append(line)
    return space

def rotate_space(arr):
    space = [list(row) for row in zip(*arr)][::-1]
    return space

def reset_space(arr):
    space = [list(row)[::-1] for row in zip(*arr)]
    return space

def manhatten(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

if __name__ == "__main__":
    D = open("input.txt").read().strip()
    lines = D.split("\n")
    space, coords = [], []
    
    for line in lines:
        space.append(list(line))

    space = rotate_space(cosmically_inflate(space))
    space = reset_space(cosmically_inflate(space))

    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == "#":
                coords.append([i,j])

    galaxy_route = []
    paths = []
    counter = 1
    for i, s_galaxy in enumerate(coords):
        star_jump = 999
        for j in range(counter, len(coords)):
            e_galaxy = coords[j]
            if s_galaxy != e_galaxy:
                distance = manhatten(s_galaxy[1], s_galaxy[0], e_galaxy[1], e_galaxy[0])
                paths.append(distance)
                if distance < star_jump:
                    star_jump = distance
        
        counter += 1
        galaxy_route.append(star_jump)
    
    print(len(galaxy_route))
    print(sum(paths))
