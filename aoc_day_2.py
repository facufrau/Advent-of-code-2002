# --- Day 2: Password Philosophy ---
# by Facundo Frau - Github: facufrau

# Part one.
passwords_1 = 0
with open('day2a_input.txt', 'r') as f:
    for l in f.readlines():
        line = l.split()
        # Numbers and the limits for repeating values of letter.
        lowest, highest = [int(x) for x in line[0].split('-')]
        letter = line[1].replace(':', '')
        password = line[2]
        
        # Check for valid passwords, number of times the letter appears.
        if lowest <= password.count(letter) <= highest:
            passwords_1 += 1

print(f"Part 1 answer: {passwords_1}")

# Part two.
passwords_2 = 0
with open('day2a_input.txt', 'r') as f:
    for l in f.readlines():
        line = l.split()
        # Number are positions for checking the letter.
        first, second = [int(x) -1 for x in line[0].split('-')]
        letter = line[1].replace(':', '')
        password = line[2]
        
        # Check for valid passwords, only one index having the letter.
        matches = 0
        if password[first] == letter:
            matches += 1
        if password[second] == letter:
            matches += 1
        
        if matches == 1:
            passwords_2 += 1

print(f"Part 2 answer: {passwords_2}")
     

