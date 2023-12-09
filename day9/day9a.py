import re

def get_intervals(line):
  return [j-i for i,j in zip(line[:-1], line[1:])]

with open('input.txt', 'r') as file:
  histories = [[int(x) for x in re.findall(r'\-*\d+', line)] for line in file]

total = 0

for his in histories:
    groups = [his]
    dif = his

    while len(set(dif)) != 1:
      dif = get_intervals(dif)
      groups.append(dif)
    
    total += sum([group[-1] for group in groups])

print(total)
