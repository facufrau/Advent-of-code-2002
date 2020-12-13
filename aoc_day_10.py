# --- Day 10: Adapter Array ---
# by Facundo Frau - Github facufrau
from math import prod

with open('day10_input.txt') as f:
    adapters = [int(x) for x in f.read().splitlines()]
    adapters.sort()
    
# Part one.
diff_3 = 1
diff_1 = 1
for i in range(len(adapters)):
    if i == len(adapters) - 1:
        break
    else:
        delta = adapters[i + 1] - adapters[i]
        if delta == 1:
            diff_1 += 1
        elif delta == 3:
            diff_3 += 1
print(f"Part 1 answer - {diff_1 * diff_3}")

# Part two.
adapters.insert(0,0)
adapters.insert(-1, max(adapters) + 3)
adapters.sort()
    
diffs = [adapters[x]-adapters[x-1] for x in range(1, len(adapters))]

sub_comb = []
elements = 0
for i in range(len(diffs)):
    if diffs[i] == 3:
        if elements == 4:
            sub_comb.append(7)
        elif elements == 3:
            sub_comb.append(4)
        elif elements == 2:
            sub_comb.append(2)
        else:
            sub_comb.append(1)
        elements = 0
    else:
        elements += 1
total_comb = prod(sub_comb)
print(f"Part 2 answer - Combinations = {total_comb}")