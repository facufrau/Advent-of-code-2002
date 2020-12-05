# --- Day 4: Passport Processing ---
# by Facundo Frau - Github facufrau
with open('day4_input.txt', 'r') as f:
    passports = {}
    new_line = ""
    counter = 1
    lines = f.readlines()

    for line in lines:
        if line == '\n':
            data = new_line.split()
            passports[counter] = {}
            for d in data:
                d = d.split(":")
                passports[counter][d[0]] = d[1]
            counter += 1
            new_line = ""
        else:
            new_line += line.replace("\n", " ")
            
# Part one
valid_passports = 0
for value in passports.values():
	if len(value) == 8:
		valid_passports += 1
	elif len(value) == 7 and ('cid' not in value):
		valid_passports += 1

print(f"Part 1 Answer - Valid passports: {valid_passports}")
	
# Part two
def valid_byr(passport):
	"""Validates byr -> 4 digits between 1920 and 2002."""
	if 'byr' in passport:
		if len(passport['byr']) == 4 and (1920 <=int(passport['byr']) <= 2002):
			return True
		else:
			return False
	else:
		return False

def valid_iyr(passport):
	"""Validates iyr -> 4 digits between 2010 and 2020."""
	if 'iyr' in passport:
		if len(passport['iyr']) == 4 and (2010 <=int(passport['iyr']) <= 2020):
			return True
		else:
			return False
	else:
		return False
		
def valid_eyr(passport):
	"""Validates eyr -> 4 digits between 1920 and 2002."""
	if 'eyr' in passport:
		if len(passport['eyr']) == 4 and (2020 <=int(passport['eyr']) <= 2030):
			return True
		else:
			return False
	else:
		return False
	
def valid_hgt(passport):
	""" A number followed by either cm or in:
		If cm, the number must be at least 150 and at most 193.
		If in, the number must be at least 59 and at most 76.
		(\d+)([a-z]{2}) REGEX
		https://stackoverflow.com/questions/11592261/check-if-a-string-is-hexadecimal
	"""
	
