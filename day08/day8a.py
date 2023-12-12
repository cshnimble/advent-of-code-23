import re

paths = { 'L': 0, 'R':1 }

# Traverse the nodes
def traverse(node, steps):
  cur_node = node
  for c in instructions:
    cur_node = mapping[cur_node][paths[c]]
  steps += len(instructions)
  return cur_node, steps

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Get the series of instructions to run
instructions = input_lines[0]

# Get all the nodes
nodes = [line.split(' = ')[0] for line in input_lines[2:]]

# Get all the next node pairs
lookup = [tuple(re.findall(r'\w{3}', line)[1:]) for line in input_lines[2:]]

# Create a mapping of all `Node : (L, R)`
mapping = { nodes[i]: lookup[i] for i in range(len(nodes)) }

steps = 0
cur_node = 'AAA'

# Brute force traversal from AAA to ZZZ
while(cur_node != 'ZZZ'):
  cur_node, steps = traverse(cur_node, steps)

print(steps)
