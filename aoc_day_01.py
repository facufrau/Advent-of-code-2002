# --- Day 1: Report Repair ---
# by Facundo Frau - Github facufrau
from itertools import permutations

# Read and convert input to a list.
with open ('day1_input.txt', 'r') as f:
    report = [int(x) for x in f.readlines()]

# Part one
def first_part(num_lst):
    """
    Check for two numbers that add up 2020 and return their product.
    """
    for i in range(len(num_lst)):
        for j in range(i + 1):
            entry = num_lst[i], num_lst[j]
            if sum(entry) == 2020:
                return entry[0] * entry[1]

print(f"Part one answer: {first_part(report)}")

# Part two
def second_part(num_lst):
    perms = list(permutations(num_lst, r=3))
    for p in perms:
        if sum(p) == 2020:
            return p[0] * p[1] * p[2]
            
print(f"Part two answer: {second_part(report)}")