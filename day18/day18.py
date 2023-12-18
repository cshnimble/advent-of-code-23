with open('test.txt', 'r') as file:
  command_list = [line.strip() for line in file]

commands = [line.split(' ')[:2] for line in command_list]

# Mark out the size of the grid
grid_size = (0,0)

ptr = (0,0)
ptrs = [ptr]

for command in commands:
  dir = command[0]
  steps = int(command[1])
  # Move the ptr
  if dir == 'D':
    ptr = (ptr[0], ptr[1] + (steps))
  elif dir == 'U':
    ptr = (ptr[0], ptr[1] - (steps))
  elif dir == 'R':
    ptr = (ptr[0] + (steps), ptr[1])
  else:
    ptr = (ptr[0] - (steps), ptr[1])

  ptrs.append(ptr)
  grid_size = (max(ptr[0], grid_size[0]), max(ptr[1], grid_size[1]))
  
# print('Grid size is {} x {}'.format(grid_size[0], grid_size[1]))
# print('Ptrs are {}'.format(ptrs))

grid = []

# Create the blank grid
for y in range(grid_size[1]+1):
  grid.append(['.'] * (grid_size[0]+1))

# Sort the ptrs into order based on Y coord
ptrs = sorted(ptrs[:-1], key=lambda x: x[1])

# Fill in the spaces
for y in range(grid_size[1] + 1):
  xs = sorted(list(filter(lambda a: a[1] == y, ptrs)), key = lambda x: x[0])
  if len(xs) == 0: continue
  # Fill in between points

# Old code, didn't work
# for x in range(grid_size[0] + 1):
#   ys = sorted(list(filter(lambda a: a[0] == x, ptrs)), key = lambda a: a[1])
#   print(ys)
#   if len(ys) == 0: continue
#   for y in range(ys[0][0], ys[0][-1] + 1):
#     grid[y][x] = '#'

for g in grid:
  print(g)

print('Part 1: {}'.format(sum(line.count('#') for line in grid)))
# Test eq 62