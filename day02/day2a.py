results = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def get_cubes_per_game(game):
    draws = [dict(reversed(d.split(' ')) for d in e) for e in [f.split(', ') for f in game.split('; ')]]
    return {
        k: [d.get(k) for d in draws]
        for k in set().union(*draws)
    }

def possible(game):
    res = True
    for k,v in results.items():
        g = ['0' if i is None else i for i in game[k]]
        res = all(int(i) <= results[k] for i in g)
        if(not res):
            break
    return res

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

games = [line[line.index(':')+1:].strip() for line in input_lines]

cubes = [get_cubes_per_game(game) for game in games]

sum = 0

for c in cubes:
    if(possible(c)):
        sum += (cubes.index(c) +1)

print(sum)