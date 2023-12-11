D = open("test.txt").read().strip()
lines = D.split("\n")

coords = []
i_iter = 0
j_iter = 0
for i, line in enumerate(lines):
    line_ar = list(line)
    if(len(set(line_ar))) == 1:
       i_iter += 2
    else:
        for j, char in enumerate(line):
            if char == "#":
                coords.append([i,j])
        i_iter+=1

print(coords)
