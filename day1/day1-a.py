import re

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

only_digits = [re.sub(r'[A-Za-z]*', '', line) for line in input_lines]

sum_digits = sum([int(line[0] + line[len(line)-1]) if len(line) >= 2 else int(line + line) for line in only_digits])

print(sum_digits)