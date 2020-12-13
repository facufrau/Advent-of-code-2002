# --- Day 10: Adapter Array ---
# by Facundo Frau - Github facufrau

with open('day10_input.txt') as f:
    adapters = [int(x) for x in f.read().splitlines()].sort()
    
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