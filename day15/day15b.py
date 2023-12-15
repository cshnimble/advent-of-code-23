import re
from collections import defaultdict

# Perform the string hash
def _hash(input):
  res = 0
  for c in input:
    res = ((res + ord(c)) * 17) % 256
  return res

with open('input.txt', 'r') as file:
  commands = file.read().strip().split(',')

# Create a default dictionary of dict[str, int]
boxes = defaultdict(dict)

for command in commands:
  tokens = re.split(r'[\-=]', command)
  lens = tokens[0]
  box = _hash(lens)
  if '-' in command:
    boxes[box].pop(lens, None)
  else:
    focal_length = int(tokens[1])
    boxes[box][lens] = focal_length

res = sum((box+1)*(slot+1)*fl for box in boxes for slot,fl in enumerate(boxes[box].values()))
  
print('Part 2: {}'.format(res))
