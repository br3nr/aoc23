import math
D = open("input.txt").read().strip()
lines = D.split("\n")

time = [int(time) for time in lines[0].split() if time.isdigit()]
distance = [int(time) for time in lines[1].split() if time.isdigit()]
record = 1

# d = (t-x) * x
# -x^2 + tx - d
    
for i in range(len(time)):
    t = time[i]
    d = distance[i]
    disc = t**2 - 4 * (-1) * (-d)

    x1 = ((-t) + math.sqrt(disc))/2*-1
    x2 = ((-t) - math.sqrt(disc))/2*-1

    if x1.is_integer() and x2.is_integer:
        num_values = (math.floor(x2) - math.ceil(x1)+1)-2
    else:
        x1 = math.ceil(x1)
        x2 = math.floor(x2)
        num_values = x2 - x1 + 1
    
    record*=num_values

print(record)
