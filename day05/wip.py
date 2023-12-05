import sys
import itertools
import time

with open('test.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

groupings = [list(group) for k, group in itertools.groupby(input_lines, lambda x: x=='') if not k]

# get the seeds
seed_list = groupings[0][0].split(':')[1].strip().split(' ')
seeds = list(zip(seed_list[0::2], seed_list[1::2]))
# seed ranges
pairs = [(int(seed[0]), int(seed[0]) + int(seed[1])-1) for seed in seeds]

# sort the maps of ranges
maps = []
for group in groupings[1:]:
  r = []
  for line in group[1:len(group)]:
    tup = tuple(line.split(' '))
    r.append(tup)
  maps.append(r)

start_time = time.time()
# Get the lowest loc
# Set loc to system max, just in case
loc = sys.maxsize
for low, high in pairs:
  print('low: {}, high: {}'.format(low,high))
  

print(loc)
print("--- %s seconds ---" % (time.time() - start_time))

# Should eq 27992443