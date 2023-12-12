import re
import math

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

# Get all the starting nodes
starting_nodes = list(filter(lambda x: x[-1] == 'A', nodes))

# Create a mapping of `Node : path length to end node` with default 0
traversal_lengths = dict(zip(cur_nodes, [0] * len(starting_nodes)))

# Traverse all nodes and find path length
for node in traversal_lengths.keys():
  steps = 0
  cur_node = node
  while(cur_node[-1] != 'Z'):
    cur_node, steps = traverse(cur_node, steps)
  traversal_lengths[node] = steps

# Find the lcm between all path lengths for the total steps needed
print(math.lcm(*traversal_lengths.values()))
