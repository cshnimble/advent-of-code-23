with open('test.txt', 'r') as file:
  records = [line.strip() for line in file]

records = [[r.strip() for r in rec.split(' ')] for rec in records]

for rec in records:
  springs = rec[0]
  groups = rec[1]
  

# Test eq 21