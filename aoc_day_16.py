# --- Day 16: Ticket Translation ---
# by Facundo Frau - Github facufrau

with open('day16_input.txt') as f:
    lines = f.read().splitlines()
    rules = {}
    for line in lines:
        # Store rules for ticket fields in a dictionary with tuples as values.
        if line == '':
            break
        else:
            line = line.replace('or','').replace('-', ' ').replace(':', '').split()
            if len(line) == 6:
                line = [int(x) if i > 1 else x for i, x in enumerate(line)]
                key = line[0] + ' ' + line[1]
                rules[key] = tuple(line[2:])
            else:
                line = [int(x) if i > 0 else x for i, x in enumerate(line)]
                rules[line[0]] = tuple(line[1:])

    # Store my ticket as a list of numbers.
    my_ticket = lines[lines.index('your ticket:') + 1].split(',')
    my_ticket = [int(x) for x in my_ticket]

    # Store nearby tickets as a list of lists.
    separator = lines.index('nearby tickets:') + 1
    nearby_tickets = []
    for line in lines[separator:]:
        ticket = [int(x) for x in line.split(',')]
        nearby_tickets.append(ticket)

# Part one
error_rate = 0
valid_tickets = []  # Used in part two.
for ticket in nearby_tickets:
    is_valid = True
    for field in ticket:
        valid = 0
        for value in rules.values():
            if (value[0] <= field <= value[1]) or (value[2] <= field <= value[3]):
                valid += 1
        if valid == 0:
            error_rate += field
            is_valid = False
    if is_valid:  
        valid_tickets.append(ticket)
print(f"Part 1 answer - Scanning error rate: {error_rate}")

# Part two
total = len(valid_tickets[0])
columns = []
for i in range(total):
    col = []
    for ticket in valid_tickets:
        col.append(ticket[i])
    columns.append(col)

# Dict for storing which columns could match which fields.
valid_columns = {}
total = len(columns[0])
for key, value in rules.items():
    for item in columns:
        counter = 0
        for i in item:
            if (value[0] <= i <= value[1]) or (value[2] <= i <= value[3]):
                counter += 1
        if counter == total:
            if key not in valid_columns:
                valid_columns[key] = [columns.index(item)]
            else:
                valid_columns[key].append(columns.index(item))

# Use total number of rules.
total_rules = len(rules)

# Function that removes repeating values in valid columns dict.
# First starts with the columns that have only 1 field matching.
# Then start removing those values and repeat until all have 1 valid field.
def remove_values(dict_rules, val):
    for k, v in dict_rules.items():
        if len(v) != 1:
            if val in dict_rules[k]:
                dict_rules[k].remove(val)

while not all(len(value) == 1 for value in valid_columns.values()):
    for fields, columns in valid_columns.items():
        if len(columns) == 1:
            remove_values(valid_columns, columns[0])

# Get final answer. Starting value = 1 for multiplying.
answer_2 = 1
for k, v in valid_columns.items():
    if k.startswith('departure'):
        answer_2 *= my_ticket[v[0]]
print(f"Part 2 answer - 'departure' fields mult: {answer_2}")