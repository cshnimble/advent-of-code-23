import sys
import itertools
import time

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

groupings = [list(group) for k, group in itertools.groupby(input_lines, lambda x: x=='') if not k]

# get the seeds
seed_list = groupings[0][0].split(':')[1].strip().split(' ')
seeds = list(zip(seed_list[0::2], seed_list[1::2]))

# sort the maps of ranges
maps = []
for group in groupings[1:]:
  dest = []
  src = []
  for line in group[1:len(group)]:
    d,s,l = line.split(' ')
    dest.append((d,l))
    src.append((s,l))
  map = {
    src[i]: dest[i] for i in range(len(src))
  }
  maps.append(map)
start_time = time.time()
# Get the lowest loc
# Set loc to system max, just in case
loc = sys.maxsize
for seed in seeds:
  seedr = range(int(seed[0]), int(seed[0])+int(seed[1]))
  for i in seedr:
    tmp = i
    for m in maps:
      for k in m.keys():
        src_min_val = int(k[0])
        src_max_val = int(k[0])+int(k[1])-1
        if src_min_val <= tmp <= src_max_val:
          # it's in the range, so find the pos
          tmp = int(m[k][0]) + (tmp - src_min_val)
          break
    if tmp <= loc:
      loc = int(tmp)

print(loc)
print("--- %s seconds ---" % (time.time() - start_time))

# 58556595 too high
# Should eq 27992443