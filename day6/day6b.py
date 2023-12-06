# Slightly more intelligent solution to 6b, still needs refining
# Brute force reduced by 1/2 as possibilities are a histogram

import re
import math

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

nums = [''.join(re.findall(r'\d+', line)) for line in input_lines]

race = (int(nums[0]), int(nums[1]))

# Solve via quadratic equation

tmp = math.sqrt(race[0]**2 - 4*race[1])
c2 = (race[0] + tmp) / 2
c1 = (race[0] - tmp) / 2
print(int(c2) - int(math.ceil(c1)) + 1)
