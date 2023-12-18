with open('test.txt', 'r') as file:
  grid = [[int(c) for c in line.strip()] for line in file]

START = (0,0)
MAX_X = len(grid[0])
MAX_Y = len(grid)
END = (MAX_X-1, MAX_Y-1)
MAX_LINE = 3

total = grid[START[1]][START[0]]
path = [START]

print(path)

print('Part 1: {}'.format(total))
# Test eq 102
