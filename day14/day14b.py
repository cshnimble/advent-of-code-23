import re

NUM_CYCLES = 1_000_000_000
CYCLE_ORDER = ['N', 'W', 'S', 'E']

# Create a cache for states
cache = {}

# Create a hash of the string representation of the grid for caching
def _hash(grid_str):
  return hash(grid_str)

# Sorts a row of rocks
# Pushes all round rocks (O) as far right as possible
def sort_rocks(row):
  splits = list(filter(None, re.split(r'(#+)', row)))
  sort_splits = []
  for split in splits:
    if '#' in split: sort_splits.extend(split)
    split = ''.join('.' * split.count('.')) + ''.join('O' * split.count('O'))
    sort_splits.extend(split)
  return ''.join(sort_splits)

# Do a full cycle with each rotation
def do_cycle(grid):
  _key = _hash(''.join(grid))
  if _key in cache.keys():
    grid = cache[_key]
    return grid
  for dir in CYCLE_ORDER:
    if dir == 'S': grid = list(reversed(grid))                          # Flip 180 degrees
    if dir == 'E': grid = list(reversed(list(zip(*grid))))              # Flip  90 degrees
    if dir == 'W': grid = [''.join(list(i)) for i in zip(*grid[::-1])]  # Flip 270 degrees

    # Rotate grid to get all cols
    cols = [''.join(list(i)) for i in zip(*grid[::-1])]

    # For all cols, find position(s) of square rocks (#) and move all round rocks towards north
    sorted_cols = []
    for col in cols:
      sort_col = sort_rocks(col)
      sorted_cols.extend([sort_col])

    # Rotate cols back
    grid = list(reversed(list(zip(*sorted_cols))))

    # Bring grid to original
    if dir == 'S': grid = list(reversed(grid))
    if dir == 'E': grid = [''.join(list(i)) for i in zip(*grid[::-1])]
    if dir == 'W': grid = list(reversed(list(zip(*grid))))

  cache[_key] = grid
  return grid

with open('input.txt', 'r') as file:
  grid = [line.strip() for line in file]

GRID_HEIGHT = len(grid)

# Do a subset of cycles to find any loop to minimise the full loop
hits = {}
grid_copy = grid
for i in range(1000):
  _key = _hash(''.join(grid_copy))
  if _key in cache.keys():
    loops = hits[_key] + 1
    loop_size = i - hits[_key]
    iters = loops + (NUM_CYCLES - loops) % loop_size
    break
  grid_copy = do_cycle(grid_copy)
  hits[_key] = i

# Now we know the loop size, just do that small loop
for i in range(iters):
  grid = do_cycle(grid)

# Get the number of round rocks per row and multiply by row number from south
total = 0
for row in grid:
  total += row.count('O') * (GRID_HEIGHT - grid.index(row))

print('Part 2: {}'.format(total))
