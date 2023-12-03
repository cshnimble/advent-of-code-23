import re

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Get all the numbers per row
nums = []

for r in input_lines:
    n = list(filter(None, re.split(r'[\D.]', r)))
    nums.append(n)

sum = 0

# Calculate the sum
for row in input_lines:
    # Get our max length values for the matrix
    x_max = len(row)
    y_max = len(input_lines)
    y_slot = input_lines.index(row)

    sanitised_line = row

    for num in nums[y_slot]:
        tmp = sanitised_line.index(num)
        x_slots = list(range(tmp, tmp + len(num)))
        # Check all neighbours
        for slot in x_slots:
            x = [row[max(0,slot-1):min(x_max,slot+2)] for row in input_lines[max(0, y_slot-1):min(y_max,y_slot+2)]]
            res = any(re.search(r'[^\d.]+', n) for n in x)
            if(res):
                sum += int(num)
                break

        repl = ''.join('.' for i in range(len(num)))
        # Get rid of the first instance of this number to stop it being found again
        sanitised_line = re.sub(num, repl, sanitised_line, 1)

print(sum)