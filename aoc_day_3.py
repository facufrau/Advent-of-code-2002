# --- Day 3: Toboggan Trajectory ---
# by Facundo Frau - Github facufrau
import time

# Part one.
with open('day3_input.txt','r') as f:
    lines = f.readlines()

    # Trees are marked '#' in lines, '.' for free space.
    trees = 0
    for line in lines:
        print(len(lines))
        print(line)
        time.sleep(3)