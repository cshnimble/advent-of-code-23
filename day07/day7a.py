from functools import cmp_to_key

# Weights based on the counts of cards needed in the hand
hand_str = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]

# Weights per card
card_str = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
weights = {val: (idx + 1) for idx, val in enumerate(card_str)}

# Returns the rank based on the number of cards in the hand
def get_hand_strength(hand):
  return hand_str.index(hand)

# Compares two players:
# If their hand scores aren't equal, return the value
# Otherwise, return the difference between the cards causing the ties
# And if that's still 0, return the default
def compare(a, b):
  if a[1] - b[1] != 0:
    return a[1] - b[1]
  
  for ca, cb in zip(a[0], b[0]):
    if weights[ca] - weights[cb] != 0:
      return card_str.index(ca) - card_str.index(cb)

  return 0

# Get the plays
with open('input.txt', 'r') as file:
  plays = [(line[0:line.index(' ')], int(line[line.index(' ')+1:])) for line in file]

# Get the player hand, score and bid
players_unranked = []
for hand, bid in plays:
  cards = { c: hand.count(c) for c in set(hand)}
  card_counts = tuple(reversed(sorted(cards.values())))
  hand_weight = get_hand_strength(card_counts)
  players_unranked.append((hand, hand_weight, bid))

# Sort the players into rank order
players_ranked = sorted(players_unranked, key=cmp_to_key(compare))

# Get the total winnings
total = sum((i+1) * p[2] for i, p in enumerate(players_ranked))

print(total)
