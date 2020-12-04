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
    print(len(passports[1]))