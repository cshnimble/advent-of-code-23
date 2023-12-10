import itertools

# Directions and their movements on the grid
compass = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}
# Valid components depending on direction travelling
valids = {
    'N': '|7F',
    'S': '|LJ',
    'E': '-J7',
    'W': '-LF'
}
# Pipe options based on joining directions
options = {
    'NS': '|',
    'NE': 'L',
    'NW': 'J',
    'SE': 'F',
    'SW': '7',
    'EW': '-'
}
# Get a list of all the next possible coordinates from `coord`
def traverse(coord):
    nexts = []
    x = grid[coord[1]][coord[0]]
    valid_dirs = 'NSEW'
    if x != 'S':
        valid_dirs = dict((v,k) for k,v in options.items())[grid[coord[1]][coord[0]]]
    for dir in valid_dirs:
        next_x = coord[0] + compass[dir][0]
        next_y = coord[1] + compass[dir][1]
        if (0 <= next_x < x_max) and (0 <= next_y < y_max):
            nxt = grid[next_y][next_x]
            if (nxt != '.') and (nxt in valids[dir]):
                nexts.append((next_x,next_y))
    return nexts

with open('input.txt', 'r') as file:
  grid = [[c for c in line.strip()] for line in file]

# Get boundary maxes
x_max = len(grid[0])
y_max = len(grid)

# Get the co-ord for the start
start = (None, None)
for line in grid:
    if 'S' in line:
        start = (line.index('S'), grid.index(line))

# Get the next possible moves
nexts = traverse(start)

# Figure out what S was
# Get directions these are in, then figure out what could possibly be and replace
l = '{}{}'.format(grid[nexts[0][1]][nexts[0][0]], grid[nexts[1][1]][nexts[1][0]])
coords = [(n[0]-start[0], n[1]-start[1])for n in nexts]
dirs = ''.join(x for x in [list(compass.keys())[list(compass.values()).index(c)] for c in coords])
S = options[dirs]
grid[start[1]][start[0]] = S

# Start up a list of valid routes
paths = nexts
paths.append(start)
looped = False

while not looped:
    nexts = list(set(list(itertools.chain(*[traverse(n) for n in nexts]))))
    nexts = list(filter(lambda x: x not in paths, nexts))
    if nexts == []:
        looped = True
    paths.extend(nexts)

print('Part 1: {}'.format(len(paths)//2))
