from collections import defaultdict

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Matrix of all chars
mat = [[c for c in line] for line in input_lines]

# Matrix of surrounding coords
sur = [-1, 0, 1]

# Get our max length values for the matrix
row_max = len(mat[0])
col_max = len(mat)

nums = defaultdict(list)

for row in range(row_max):
    gears = set()
    n = 0
    part = False

    for col in range(col_max + 1):
        if col < col_max and mat[row][col].isdigit():
            n = n * 10 +int(mat[row][col])
            for prow in sur:
                for pcol in sur:
                    if 0 <= col + pcol < col_max and 0 <= row + prow < row_max:
                        char = mat[row+prow][col+pcol]
                        if not char.isdigit() and char != '.':
                            part = True
                        if char == '*':
                            gears.add((row+prow, col+pcol))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            n = 0
            part = False
            gears = set()

res = 0
for k,v in nums.items():
  if len(v)==2:
    res += v[0] * v[1]

print(res)