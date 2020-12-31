# --- Day 13: Shuttle Search ---
# by Facundo Frau - Github facufrau
from math import prod

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
schedule = {}
for bus in buses:
    if bus == 'x':
        continue
    else:
        schedule[bus] = buses.index(bus)

# Help and idea for solving the CRT taken from this video in youtube.
# https://www.youtube.com/watch?v=zIFehsBHB8o - Maths with jay channel.

def solve_system(buses_schedule):
    # Initialize data structures for table.
    N_value = prod(buses_schedule.keys())
    b_list = []
    Ni_list = []
    xi_list = []
    # Calculate bi elements
    for k, v in buses_schedule.items():
        if v == 0:
            b_list.append(v)
        else:
            b_list.append(k-v)
    # Calculate Ni elements
    for k in buses_schedule.keys():
        Ni_list.append(N_value // k)
    # Calculate xi elements
    for i,n in enumerate(Ni_list):
        mod = N_value // Ni_list[i]
        xi_list.append(pow(n, -1, mod))
    # Calculate final products
    final_values = []
    for i in range(len(b_list)):
        prod_b_n_i = b_list[i] *  Ni_list[i] * xi_list[i]
        final_values.append(prod_b_n_i)
    return sum(final_values) % N_value
   
answer_2 = solve_system(schedule)
print(f"Part two - Timestamp T for requirements: {answer_2}")
