# --- Day 8: Handheld Halting ---
# by Facundo Frau - Github facufrau
import copy
import sys

with open('day8_input.txt') as f:
    lines = [line.strip('\n').split(' ') for line in f]

# Part one
# Variable for storing acc value and keep track of orders executed.
accumulator = 0
executed = set()
index = 0
while True:
    order = lines[index][0]
    value = int(lines[index][1])
    if index in executed:
        break
    executed.add(index)
    if order == 'acc':
        accumulator += value
        index += 1
    elif order == 'nop':
        index += 1
    elif order == 'jmp':
        index += value
print(f"Part one answer - accumulator value: {accumulator}")

# Part two.
mod = 0
while mod < len(lines):
    orders = copy.deepcopy(lines)
    if orders[mod][0] == 'nop':
        orders[mod][0] = 'jmp'
    elif orders[mod][0] == 'jmp':
        orders[mod][0] = 'nop'
    
    accumulator = 0
    executed = set()
    index = 0
    while True:
        order = orders[index][0]
        value = int(orders[index][1])
        if index in executed:
            break
        executed.add(index)
        try:
            orders[index + 1]
        except IndexError:
            print(f"Part two answer - accumulator value: {accumulator}")
            sys.exit(0)
        if order == 'acc':
            accumulator += value
            index += 1
        elif order == 'nop':
            index += 1
        elif order == 'jmp':
            index += value
    mod += 1