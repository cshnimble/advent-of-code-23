import re

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

with open('input.txt', 'r') as file:
  grid = [line.strip() for line in file]

GRID_HEIGHT = len(grid)

# Rotate grid to get all cols
cols = [''.join(list(i)) for i in zip(*grid[::-1])]

# For all cols, find position(s) of square rocks (#) and move all round rocks towards north
sorted_cols = []
for col in cols:
  sort_col = sort_rocks(col)
  sorted_cols.extend([sort_col])

# Rotate cols back
sort_grid = list(reversed(list(zip(*sorted_cols))))

# Get the number of round rocks per row and multiply by row number from south
total = 0
for row in sort_grid:
  total += row.count('O') * (GRID_HEIGHT - sort_grid.index(row))

print('Part 1: {}'.format(total))
