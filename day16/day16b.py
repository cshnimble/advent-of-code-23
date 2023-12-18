# Look at the next step
def next_step(coord):
  nexts = []
  route = DIRECTIONS[coord[2]]
  next = (coord[0] + route[0], coord[1] + route[1])
  if (0 <= next[0] < MAX_X) and (coord[2] in 'EW'):
    if grid[next[1]][next[0]] == '.' or grid[next[1]][next[0]] == '-':
      nexts.append((next[0], next[1], coord[2]))
    elif grid[next[1]][next[0]] == '/':
      if coord[2] == 'E':
        nexts.append((next[0], next[1], 'N'))
      else:
        nexts.append((next[0], next[1], 'S'))
    elif grid[next[1]][next[0]] == '\\':
      if coord[2] == 'E':
        nexts.append((next[0], next[1], 'S'))
      else:
        nexts.append((next[0], next[1], 'N'))
    else:
      nexts = [(next[0], next[1], 'N'), (next[0], next[1], 'S')]
  elif (0 <= next[1] < MAX_Y) and (coord[2] in 'NS'):
    if grid[next[1]][next[0]] == '.' or grid[next[1]][next[0]] == '|':
      nexts.append((next[0], next[1], coord[2]))
    elif grid[next[1]][next[0]] == '/':
      if coord[2] == 'N':
        nexts.append((next[0], next[1], 'E'))
      else:
        nexts.append((next[0], next[1], 'W'))
    elif grid[next[1]][next[0]] == '\\':
      if coord[2] == 'N':
        nexts.append((next[0], next[1], 'W'))
      else:
        nexts.append((next[0], next[1], 'E'))
    else:
      nexts = [(next[0], next[1], 'E'), (next[0], next[1], 'W')]
  return nexts

with open('input.txt', 'r') as file:
  grid = [[i for i in line.strip()] for line in file]

# Starting coord and direction heading
START = (-1,0, 'E')
MAX_X = len(grid[0])
MAX_Y = len(grid)
DIRECTIONS = {
  'N' : (0,-1),
  'S' : (0, 1),
  'E' : (1, 0),
  'W' : (-1,0)
  }

# Build up a list of the energised tiles
energised_tiles = []
max_tiles = 0

complete = False
coords = [START]

while not complete:
  nexts = []
  for coord in coords:
    nexts = nexts + next_step(coord)
  nexts = list(filter(lambda x: x not in energised_tiles, nexts))
  if nexts == []:
    complete = True
  energised_tiles = energised_tiles + nexts
  energised_tiles = list(filter(None, energised_tiles))
  coords = nexts

max_tiles = max(max_tiles, len(list(set(map(lambda x: (x[0],x[1]), energised_tiles)))))

print('Part 2: {}'.format(max_tiles))
# Test eq 51