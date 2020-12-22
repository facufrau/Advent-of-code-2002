# --- Day 14: Docking Data ---
# by Facundo Frau - Github facufrau
import re
from itertools import product

with open ('day14_input.txt') as f:
    instructions = []
    for line in f.readlines():
        key, value = line.strip().split(' = ')
        if key == "mask":
            instructions.append(("mask", value))
        else:
            result = int(re.findall(r"\d+", key)[0])
            instructions.append((result, int(value)))

# Part one
def to_bin(value):
    bin_value = bin(value)[2:].zfill(36)
    return bin_value

def apply_mask(mask, value):
    new_value = ""
    for i, m in enumerate(mask):
        if m == 'X':
            new_value += value[i]
        elif m == '0':
            new_value += '0'
        elif m == '1':
            new_value += '1'
    return int(new_value, 2)

memory = {}
mask = ""
for orders in instructions:
    if orders[0] == "mask":
        mask = orders[1]
    else:
        bin_value = to_bin(orders[1])
        masked_int = apply_mask(mask, bin_value)
        memory[orders[0]] = masked_int

part1_answer = sum(memory.values())
print(f"Part one answer - sum of values = {part1_answer}")

# Part two.
memory = {}
mask = ""
for orders in instructions:
    if orders[0] == "mask":
        mask = orders[1]
    else:
        bin_address = to_bin(orders[0])
        new_address = ""
        x_indexes = []

        for i, char in enumerate(mask):
            if char == '0':
                new_address += bin_address[i]
            else:
                new_address += mask[i]
                if char == 'X':
                    x_indexes.append(i)
                    
        c = product(range(2), repeat=len(x_indexes))
        combinations = [x for x in c]
        for comb in combinations:
            addr_lst = list(new_address)
            for i, index in enumerate(x_indexes):
                addr_lst[index] = str(comb[i])
            int_addr = int(''.join(addr_lst), 2)
            memory[int_addr] = orders[1]

part2_answer = sum(memory.values())
print(f"Part two answer - sum of values = {part2_answer}")