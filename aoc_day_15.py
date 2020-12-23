# --- Day 15: Rambunctious Recitation ---
# by Facundo Frau - Github facufrau
starting = [13,16,0,12,15,1]

def memory_game(start_numbers, goal):
    last_turn = {}
    turn = 1
    for n in start_numbers:
        last_turn[n] = turn
        turn += 1
    n = start_numbers[-1]

    while turn <= goal:
        if n not in last_turn:
            last_turn[n] = turn - 1
            n = 0
        else:
            next = (turn - 1) - last_turn[n]
            last_turn[n] = turn - 1
            n = next
        turn += 1
    return n

part_one = memory_game(starting, 2020)
print(f"Part one answer - {part_one}")

part_two = memory_game(starting, 30000000)
print(f"Part two answer - {part_two}")
