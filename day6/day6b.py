# Slightly more intelligent solution to 6b, still needs refining
# Brute force reduced by 1/2 as possibilities are a histogram

import re

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

nums = [''.join(re.findall(r'\d+', line)) for line in input_lines]

race = (int(nums[0]), int(nums[1]))

wins_count = 0

# Acts as a histogram so only check half and double the result
half = int(race[0]/2)

# No point doing 0 or max seconds as no movement
for i in range(0,half+1):
  res = i * (int(race[0]) - i)
  multiplier = 2
  # Exact middle not needing duplicating
  if (i == half) and (i % 2 != 0):
    multiplier = 1
  if res > int(race[1]): wins_count += multiplier

print(wins_count)
