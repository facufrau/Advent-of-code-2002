# --- Day 15: Rambunctious Recitation ---
# by Facundo Frau - Github facufrau

starting = [13,16,0,12,15,1]
numbers = []
turn = 1
for n in starting:
    numbers.append(n)
    turn += 1

while turn <= 2020:
    n = numbers[-1]
    if n not in numbers[:-1]:
        numbers.append(0)
        turn += 1
    else:
        indexes = [(i + 1) for i, x in enumerate(numbers) if x == n]
        next = (turn - 1) - indexes[-2]
        numbers.append(next)
        turn += 1
print(f"Part one answer - {numbers[-1]}")
