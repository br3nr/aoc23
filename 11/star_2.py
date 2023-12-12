def cosmically_inflate(arr, i_inflate, j_inflate):
    space = []
    for i in range(len(arr)):
        i_sum, j_sum = 0,0
        for i_f in i_inflate:
            if arr[i][1] > i_f:
                i_sum += 999999
        for j_f in j_inflate:
            if arr[i][0] > j_f:       
                j_sum += 999999
        arr[i][0]+=j_sum
        arr[i][1]+=i_sum
    return space

def get_inflations(arr):
    inflations = []
    for i,line in enumerate(arr):
        if len(set(line)) == 1:
            inflations.append(i)
    return inflations

def rotate_space(arr):
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

    j_inflate = get_inflations(space)
    i_inflate = get_inflations(rotate_space(space)) # :3
    
    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == "#":
                coords.append([i,j])

    cosmically_inflate(coords, i_inflate, j_inflate)
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
                print(s_galaxy, e_galaxy, distance)
                if distance < star_jump:
                    star_jump = distance
        
        counter += 1
        galaxy_route.append(star_jump)
    
    print(len(galaxy_route))
    print(sum(paths))
