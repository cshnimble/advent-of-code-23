import re

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

nums = [re.findall(r'\d+', line) for line in input_lines]

races = list(zip(nums[0], nums[1]))

wins_count = 0
for race in races:
  poss = 0
  for i in range(0,int(race[0])):
    res = i * (int(race[0]) - i)
    if res > int(race[1]): poss += 1
  if poss == 0: continue
  if wins_count == 0: wins_count += 1
  wins_count = wins_count * poss

print(wins_count)
