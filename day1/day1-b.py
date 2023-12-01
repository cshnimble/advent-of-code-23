import re

def transform_str(ln):
  f = False
  old = ln
  while not f:
    new = word_to_digit(old)
    if(old == new):
      f = True
    else:
      old = new
  return old

def word_to_digit(ln):
  ints = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  x = [ln.find(idx) for idx in ints]
  pos = smallest(x)
  if pos != None:
    unit = x.index(pos)
    # stick the int in to break up the word without breaking following numbers
    if pos == 0:
      return ln[pos] + str(ints.index(ints[unit]) + 1) + ln[pos+2:]
    else:
      return ln[:pos] + str(ints.index(ints[unit]) + 1) + ln[pos+1:]
  else:
    return ln

def smallest(lst):
  sm = None
  for i in lst:
      if i >= 0 and (sm is None or sm > i):
        sm = i
  return sm

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

convert_lines = [transform_str(line) for line in input_lines]

only_digits = [re.sub(r'[A-Za-z]*', '', line) for line in convert_lines]

sum_digits = sum([int(line[0] + line[len(line)-1]) if len(line) >= 2 else int(line + line) for line in only_digits])

print(sum_digits)