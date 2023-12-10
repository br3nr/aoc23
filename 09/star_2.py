D = open("input.txt").read().strip()
lines = D.split("\n")

def loop_line(sequence):
    new_sec = []
    for i in range(len(sequence)-1):
        new_sec.append((sequence[i+1] - sequence[i]))

    all_zero = all(val == 0 for val in new_sec)
    if not all_zero:
        print(new_sec)
        return loop_line(new_sec) + new_sec[-1]
    else:
        return new_sec[-1]

ans = 0
for line in lines:
    line = [int(x) for x in line.split(" ")]
    line.reverse()
    ans += loop_line(line) + line[-1]

print(ans)
