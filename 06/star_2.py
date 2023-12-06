import math
D = open("input.txt").read()
lines = D.split("\n")
t = int(lines[0].split(":")[1].strip().replace(" ",""))
d = int(lines[1].split(":")[1].strip().replace(" ",""))

disc = t**2 - 4 * (-1) * (-d)
x1 = ((-t) + math.sqrt(disc))/2*-1
x2 = ((-t) - math.sqrt(disc))/2*-1

if x1.is_integer() and x2.is_integer:
    num_values = (math.floor(x2) - math.ceil(x1)+1)-2
else:
    x1 = math.ceil(x1)
    x2 = math.floor(x2)
    num_values = x2 - x1 + 1

print(num_values)
