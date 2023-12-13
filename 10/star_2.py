
DIRECTION = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, -1], [0, 1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    "7": [[1, 0], [0, -1]],
    "S": [[1, 0], [-1, 0], [0, 1], [0, -1]],
}

def main():
    D = open("input.txt").read().strip()
    lines = D.split("\n")
    map = []
    S_I, S_J = 0, 0

    for i, line in enumerate(lines):
        line_arr = list(line)
        for j, pipe in enumerate(line_arr):
            if pipe == "S":
                S_I = i
                S_J = j
        map.append(line_arr)

    start_pipe = [S_I, S_J]

    interior_points = loop_start_pipes([S_I, S_J], map)
    print(interior_points)


def get_next_pipes(s_pipe, s_pipe_coords, map):  # Find valid starting pipes
    exits = DIRECTION[s_pipe]
    next_pipes = []
    for ex in exits:
        adj_i = s_pipe_coords[0] + ex[0]
        adj_j = s_pipe_coords[1] + ex[1]
        if adj_j >= 0 and adj_i >= 0:
            adj_c = map[adj_i][adj_j]
            if adj_c != ".":
                entrances = DIRECTION[adj_c]
                for entrance in entrances:
                    sum_coord = [entrance[0] + adj_i, entrance[1] + adj_j]
                    if sum_coord == s_pipe_coords:
                        next_pipes.append([adj_i, adj_j])
    return next_pipes


def loop_start_pipes(start_pipe, map):
    # Test each possible start pipe configuration
    for pipe in DIRECTION:
        DIRECTION["S"] = DIRECTION[pipe]
        next_pipes = get_next_pipes(pipe, start_pipe, map)

        if len(next_pipes) == 2:
            cycle_pipes = find_cycle(start_pipe, next_pipes, map)
            if len(cycle_pipes) > 0:
                return get_interior_points(cycle_pipes)


def get_interior_points(cycle_pipes):
    # shoelace + Picks
    laces = 0
    for i in range(len(cycle_pipes)-1):
        laces += cycle_pipes[i][0] * cycle_pipes[i+1][1] -(cycle_pipes[i][1] * cycle_pipes[i+1][0]) 
    
    return (laces/2) + 1 - ((len(cycle_pipes)-1)/2)
    


def find_cycle(start_pipe, next_pipes, map):
    cycle_pipes = []
    path = False
    cycle_found = False
    cur_pipe = next_pipes[0]
    prev_pipe = start_pipe
    cur_pipe_char = map[cur_pipe[0]][cur_pipe[1]]
    cycle_pipes.append(prev_pipe)
    cycle_pipes.append(cur_pipe)

    while not path and not cycle_found:
        exits = DIRECTION[cur_pipe_char]
        found = False
        for ex in exits:
            if not found:
                adj_pipe = [cur_pipe[0] + ex[0], cur_pipe[1] + ex[1]]
                adj_c = map[adj_pipe[0]][adj_pipe[1]]
                if adj_pipe != prev_pipe:
                    if (
                        adj_pipe[1] >= 0
                        and adj_pipe[0] >= 0
                        and adj_pipe[0] < len(map)
                        and adj_pipe[1] < len(map[0])
                    ):
                        if adj_c == "S":
                            cycle_pipes.append(adj_pipe)
                            cycle_found = True

                        elif adj_c != ".":
                            entrances = DIRECTION[adj_c]
                            for entrance in entrances:
                                position = [entrance[0] + adj_pipe[0], entrance[1] + adj_pipe[1]]
                                if position == cur_pipe:
                                    cycle_pipes.append(adj_pipe)
                                    prev_pipe = cur_pipe
                                    cur_pipe = adj_pipe
                                    cur_pipe_char = adj_c
                                    found = True
                    else:
                        path = True
                        cycle_pipes = []
    return cycle_pipes


if __name__ == "__main__":
    main()

