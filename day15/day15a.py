with open('input.txt', 'r') as file:
  commands = file.read().strip().split(',')

res = 0
for command in commands:
  cur = 0
  for c in command:
    cur = ((cur + ord(c)) * 17) % 256
  res += cur

print('Part 1: {}'.format(res))
