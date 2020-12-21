# --- Day 13: Shuttle Search ---
# by Facundo Frau - Github facufrau
from math import gcd
import itertools
# Part one.
with open('day13_input.txt') as f:
    timestamp = int(f.readline())
    buses = [int(x) for x in f.readline().split(',') if x != 'x']
buses_freq = {}
for bus in buses:
    next_freq = ((timestamp // bus) + 1) * bus -  timestamp
    buses_freq[bus] = next_freq
bus_id = min(buses_freq, key=buses_freq.get)
answer = bus_id * buses_freq[bus_id]
print(f"Part one - ID earliest bus times minutes waiting: {answer}")

# Part two.
with open('day13_input.txt') as f:
    buses = [x for x in f.readlines()[1].split(',')]
    buses = [int(x) if x != 'x' else x for x in buses ]
    print(buses)
schedule = {}
for bus in buses:
    if bus == 'x':
        continue
    else:
        schedule[bus] = buses.index(bus)
print(schedule)
#TODO - COMPLETE PART 2