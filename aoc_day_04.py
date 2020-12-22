# --- Day 4: Passport Processing ---
# by Facundo Frau - Github facufrau

with open('day4_input.txt', 'r') as f:
    passports = []
    new_line = ""
	
    lines = f.readlines()
    for line in lines:
        if line == '\n':
            passport_data = {}
            for data in new_line.split():
                data = data.split(":")
                passport_data[data[0]] = data[1]
            passports.append(passport_data)
            new_line = ""
        else:
            new_line += line.replace("\n", " ")

# Part one
valid_passports = 0
for passport in passports:
	if len(passport) == 8:
		valid_passports += 1
	elif len(passport) == 7 and ('cid' not in passport):
		valid_passports += 1
print(f"Part 1 Answer - Valid passports: {valid_passports}")
	
# Part two
def valid_byr(passport):
	"""Validates byr -> 4 digits between 1920 and 2002."""
	return ('byr' in passport) and (len(passport['byr']) == 4 and (1920 <= int(passport['byr']) <= 2002))

def valid_iyr(passport):
	"""Validates iyr -> 4 digits between 2010 and 2020."""
	return ('iyr' in passport) and (len(passport['iyr']) == 4 and (2010 <= int(passport['iyr']) <= 2020))
		
def valid_eyr(passport):
	"""Validates eyr -> 4 digits between 2020 and 2030."""
	return ('eyr' in passport) and (len(passport['eyr']) == 4 and (2020 <= int(passport['eyr']) <= 2030))

def valid_hgt(passport):
	"""Validates hgt: a number + unit (cm or in)"""
	if 'hgt' in passport:
		un = passport['hgt'][-2:]
		ht = passport['hgt'][:-2]
		if ht.isdigit():
			ht = int(ht)
			return (un == 'cm' and (150 <= ht <= 193)) or (un == 'in' and (59 <= ht <= 76))
		return False
	return False

def valid_hcl(passport):
	"""Validates hexadecimal color."""
	if 'hcl' in passport:
		hcl = passport['hcl']
		return (hcl[0] == "#" and all([x in 'abcdef0123456789' for x in hcl[1:]]))
	return False

def valid_ecl(passport):
	"""Validates ecl in list of colors."""
	colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if 'ecl' in passport:
		return passport['ecl'] in colors
	return False

def valid_pid(passport):
	"""Validates 9 digit number for pid."""
	if 'pid' in passport:
		return len(passport['pid']) == 9 and passport['pid'].isdigit()
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
for passport in passports:
	if check_passport(passport):
		valid_passports += 1
print(f"Part 2 Answer - Valid passports: {valid_passports}")