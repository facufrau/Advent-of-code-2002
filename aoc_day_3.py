# --- Day 3: Toboggan Trajectory ---
# by Facundo Frau - Github facufrau

# Part one.
# Trees are marked '#' in lines, '.' for open squares.
trees = 0

with open('day3_input.txt','r') as f:
    lines = f.read().splitlines()

row = 0  # Row for iterating over lines
block = 0  # Row for iterating along each line.

while row < len(lines) - 1:
    row += 1
    block += 3
    if block > 30:
        block = block % 31
        if lines[row][block] == '#':
            trees += 1
    else:
        if lines[row][block] == '#':
            trees += 1

print(f"Part 1 answer - N° Trees: {trees}")