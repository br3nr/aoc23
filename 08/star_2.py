from typing import List

class Node:
    def __init__(self, node):
        self.steps = 0
        self.node = node
        self.cycle_found = False

import math

D = open("input.txt").read().strip()
lines = D.split("\n")
instructions, elements = D.split("\n\n")
elements = elements.split("\n")
instructions = list(instructions)
map = {}
cur_node = "AAA"
steps = 0
over = False
start_nodes: List[Node] = []
end_nodes = []

for element in elements:    
    node, children = element.split("=")
    node = node.strip()
    if node[2] == "A":
        start_nodes.append(Node(node))
    elif node[2] == "Z":
        end_nodes.append(Node(node))

    children = children.strip()[1:-1].split(", ")
    map[node.strip()] = children

while not all(node.cycle_found for node in start_nodes):
    for dir in instructions:
        for node in start_nodes:
            if not node.cycle_found:
                node.steps += 1
                node.node = map[node.node][0] if dir == "L" else map[node.node][1]
                if node.node[2] == "Z":
                    node.cycle_found = True

steps = [node.steps for node in start_nodes]
print(math.lcm(*steps))
