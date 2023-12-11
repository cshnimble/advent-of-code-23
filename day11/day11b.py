with open('input.txt', 'r') as file:
  space = [line.strip() for line in file]

galaxies = []

# Find all rows and cols without galaxies (#)
# Also find all galaxies in row
double_rows = []
ct = 0
for r in space:
  if '#' not in r:
    double_rows.append(ct)
  g =[i for i,ltr in enumerate(r) if ltr == '#']
  for i in g:
    galaxies.append((ct, i))
  ct += 1

double_cols = []
ct = 0
for c in range(len(space[0])):
  line = ''.join([s[c] for s in space])
  if '#' not in line:
    double_cols.append(ct)
  ct += 1

# Find the distance between all galaxies
total = 0
expansion_const = 999999
for g in galaxies:
  if galaxies.index(g) == len(galaxies)-1: continue
  conns = galaxies[galaxies.index(g)+1:]
  for con in conns:
    vector = (abs(con[0]-g[0]), abs(con[1]-g[1]))
    extra_steps = 0
    for dr in double_rows:
      rng = sorted([g[0], con[0]])
      if rng[0] <= dr < rng[1]:
        extra_steps += expansion_const
    for dc in double_cols:
      rng = sorted([g[1], con[1]])
      if rng[0] <= dc < rng[1]:
        extra_steps += expansion_const

    total += extra_steps + vector[0] + vector[1]

print(total)
