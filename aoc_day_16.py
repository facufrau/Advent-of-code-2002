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
    print(rules)

    # Store my ticket as a list of numbers.
    my_ticket = lines[lines.index('your ticket:') + 1].split(',')
    my_ticket = [int(x) for x in my_ticket]

    # Store nearby tickets as a list of lists.
    separator = lines.index('nearby tickets:') + 1
    nearby_tickets = []
    for line in lines[separator:]:
        ticket = [int(x) for x in line.split(',')]
        nearby_tickets.append(ticket)
#print(nearby_tickets)

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
print(valid_tickets)

# Part two
total = len(valid_tickets)
field_order = {}

columns = []
for i in range(total):
    col = []
    for ticket in valid_tickets:
        col.append(ticket[i])
    columns.append(col)

print(columns)
for key, value in rules.items():
    for item in columns:
        counter = 0
        for i in item:
            if (value[0] <= i <= value[1]) or (value[2] <= i <= value[3]):
                counter += 1
        if counter == total:
            field_order[key] = columns.index(item)
print(field_order)

        