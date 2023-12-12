with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Get lists of numbers
games = [line[line.index(':')+1:].strip() for line in input_lines]
winners_list = [list(filter(None, game[:game.index('|')].strip().split(' '))) for game in games]
card_list = [list(filter(None, game[game.index('|')+1:].strip().split(' '))) for game in games]

# Add the initial scratchcards 
scratchcards = dict(zip(range(len(games)), [1] * len(games)))

for winners in winners_list:
  game_no = winners_list.index(winners)
  points = 0
  for num in winners:
    if num in card_list[game_no]:
      points += 1
  if(points > 0):
    new_cards = range(game_no+1, game_no+1+points)
    for i in new_cards: 
      scratchcards[i] += scratchcards[game_no]

print(sum(scratchcards.values()))