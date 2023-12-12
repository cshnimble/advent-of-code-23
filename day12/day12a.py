import re

# Split each record into the spring list and a list of groupings
def parse(record):
  a, b = record.split(' ')
  return a, list(map(int, b.split(',')))

# Find all the arrangements given a row and the groupings
def find_arrangements(s, g):
  if len(groups) == 0: return 0

  g_next = g[0]
  g_rest = g[1:]
  len_g_rest = sum(g_rest) + len(g_rest)

  print('Next: {}, rest: {}, remaining length: {}'.format(g_next, g_rest, len_g_rest))

  return 0

with open('test.txt', 'r') as file:
  records = [line.strip() for line in file]

# Create a list of lines and groupings for all records
records = [parse(rec) for rec in records]

arrangements = 0

# Get the number of arrangements per record
for springs, groups in records:
  arrangements += find_arrangements(springs, groups)

print('Part 1: {}'.format(arrangements))

# Test eq 21