# --- Day 4: Passport Processing ---
# by Facundo Frau - Github facufrau
import re

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
	"""Validates eyr -> 4 digits between 2020 and 2030."""
	if 'eyr' in passport:
		if len(passport['eyr']) == 4 and (2020 <=int(passport['eyr']) <= 2030):
			return True
		else:
			return False
	else:
		return False
	
def valid_hgt(passport):
	"""Validates hgt: a number + unit (cm or in)"""
	if 'hgt' in passport:
		prog = re.compile(r"(\d+)([a-z]{2})$")
		result = prog.match(passport['hgt'])
		if not result:
			return False
		else:
			height = int(result[1])
			unit = result[2]
			if unit == 'in':
				if 59 <= height <= 76:
					return True
				else:
					return False
			if unit == 'cm':
				if 150 <= height <= 193:
					return True
				else:
					return False
	else:
		return False

def valid_hcl(passport):
	"""Validates hexadecimal color."""
	if 'hcl' in passport:
		color = passport['hcl'].strip('#')
		if len(color) == 6:
			try:
				color = int(color, 16)
				return True
			except ValueError:
				return False
		else:
			return False
	else:
		return False

def valid_ecl(passport):
	"""Validates ecl in list of colors."""
	colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if 'ecl' in passport:
		if passport['ecl'] in colors:
			return True
		else:
			return False
	else:
		return False

def valid_pid(passport):
	"""Validates 9 digit number for pid."""
	if 'pid' in passport:
		if len(passport['pid']) == 9:
			try:
				int(passport['pid'])
				return True
			except ValueError:
				return False
		else:
			return False
	else:
		return False

def check_passport(passport):
	if not valid_byr(passport):
		return False
	elif not valid_iyr(passport):
		return False
	elif not valid_eyr(passport):
		return False
	elif not valid_hgt(passport):
		return False
	elif not valid_hcl(passport):
		return False
	elif not valid_ecl(passport):
		return False
	elif not valid_pid(passport):
		return False
	else:
		return True

valid_passports = 0
for value in passports.values():
	if check_passport(value):
		valid_passports += 1

print(f"Part 2 Answer - Valid passports: {valid_passports}")