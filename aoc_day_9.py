# --- Day 9: Encoding Error ---
# by Facundo Frau - Github facufrau
from itertools import permutations

with open('day9_input.txt') as f:
    numbers = [int(x) for x in f.read().splitlines()]

# Part one.
start = 0
stop = 25
for num in numbers[25:]:
    preamble = numbers[start:stop]
    pairs_sum = [sum(x) for x in permutations(preamble, 2)]
    if num not in pairs_sum:
        invalid = num
        print(f"Part 1 answer - invalid number: {invalid}")
        break
    else:
        start += 1
        stop += 1

# Part two.
def add_numbers(nums_list, length, goal):
    start = 0
    stop = length
    while stop <= len(nums_list):
        total = sum(nums_list[start:stop])
        if total == goal:
            return nums_list[start:stop]
        start += 1
        stop += 1
    return []

for i in range(2, len(numbers)):
    weak_nums = add_numbers(numbers, i, invalid)
    if weak_nums:
        break
p2_answer = min(weak_nums) + max(weak_nums)
print(f"Part 2 answer - encryption weakness: {p2_answer}")