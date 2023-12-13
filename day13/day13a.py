from itertools import groupby

def pair_match(pattern):
  idx = -1
  for i in range(len(pattern) -1):
    if(pattern[i] == pattern[i+1]):
      idx = i                   # Pattern found
  if idx == -1: return 0        # No pattern found
  pairs = list(zip(pattern[idx::-1], pattern[idx+1::1]))
  for pair in pairs:
    if(pair[0] != pair[1]):
      return 0                  # Pair mis-match
  return idx + 1

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Get each pattern
patterns = [list(g) for k, g in groupby(input_lines, key=bool) if k]

total = 0
# Check rows
for pattern in patterns:
  total += pair_match(pattern) * 100

# Check cols
for pattern in patterns:
  # Rotate the pattern by 90 degrees
  pattern = list(zip(*pattern[::-1]))
  total += pair_match(pattern)

print(total)
# Test eq 405
# 36226 too low