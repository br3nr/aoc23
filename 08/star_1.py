D = open("input.txt").read().strip()
lines = D.split("\n")

instructions, elements = D.split("\n\n")
elements = elements.split("\n")
instructions = list(instructions)
map = {}
cur_node = "AAA"
steps = 0
over = False

for element in elements:    
    node, children = element.split("=")
    node = node.strip()
    children = children.strip()[1:-1].split(", ")
    map[node.strip()] = children

while not over:
    for dir in instructions:
        steps += 1
        next_node = map[cur_node]
        cur_node = next_node[0] if dir == "L" else next_node[1]
        if cur_node == "ZZZ": 
            over = True

print(steps)
