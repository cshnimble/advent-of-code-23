cube_types = [
    'red',
    'green',
    'blue'
]

def get_cubes_per_game(game):
    draws = [dict(reversed(d.split(' ')) for d in e) for e in [f.split(', ') for f in game.split('; ')]]
    return {
        k: [d.get(k) for d in draws]
        for k in set().union(*draws)
    }

def get_powers(game):
    pwr = 1
    for k in cube_types:
        g = ['0' if i is None else i for i in game[k]]
        g = [int(i) for i in g]
        pwr *= int(max(g))
    return pwr

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

games = [line[line.index(':')+1:].strip() for line in input_lines]

cubes = [get_cubes_per_game(game) for game in games]

sum = 0

for c in cubes:
    sum += get_powers(c)

print(sum)