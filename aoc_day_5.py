# --- Day 5: Binary Boarding ---
# by Facundo Frau - Github facufrau
ROWS = [x for x in range(128)]
COLS = [x for x in range(8)]

# Part one.
with open('day5_input.txt') as f:
    max_id = 0
    id_nums = []
    for line in f:
        seat_row = ROWS[:]
        seat_col = COLS[:]
        for c in line:
            if c == 'F':
                seat_row = seat_row[:len(seat_row) // 2]
            elif c == 'B':
                seat_row = seat_row[len(seat_row) // 2:]
            elif c == 'L':
                seat_col = seat_col[:len(seat_col) // 2]
            elif c == 'R':
                seat_col = seat_col[len(seat_col) // 2:]

        seat_id = seat_row[0] * 8 + seat_col[0]
        id_nums.append(seat_id)
        if seat_id > max_id:
            max_id = seat_id
print(f"Part one answer - max ID: {seat_id}")
# Part two.
id_nums.sort()
for n in id_nums[1:-1]:
    if (n + 1) not in id_nums:
        print(f"Part two answer - My ID: {n + 1}")  
#print(id_nums)