with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Get lists of numbers
games = [line[line.index(':')+1:].strip() for line in input_lines]
winners_list = [list(filter(None, game[:game.index('|')].strip().split(' '))) for game in games]
card_list = [list(filter(None, game[game.index('|')+1:].strip().split(' '))) for game in games]

total = 0

for winners in winners_list:
  game_no = winners_list.index(winners)
  points = 0
  for num in winners:
    if num in card_list[game_no]:
      if points > 0:
        points *= 2
      else:
        points += 1
  total += points

print(total)