# --- Day 11: Seating System ---
# by Facundo Frau - Github facufrau
# PART TWO
import copy

with open('day11_input.txt') as f:
	seats = [list(x) for x in f.read().splitlines()]

def visible(x, y, grid):
	"""Calculates the occupied seats for one cell at grid."""
	neighs = [[-1, -1], [0, -1], [1, -1],
	          [-1, 0],           [1, 0], 
	          [-1, 1],  [0, 1],   [1, 1]]
	occupied = 0
	for n in neighs:
		k = 1
		while True:
			new_x = n[0] * k + x
			new_y = n[1] * k + y
			if (0 <= new_x <= len(grid[0]) - 1) and (0 <= new_y <= len(grid) - 1):
				state = grid[new_y][new_x]
				if state != '.':
					if state == '#':
						occupied += 1
						break
					elif state == 'L':
						break
				else:
					k += 1
			else:
				break
	return occupied
	
def next_state(grid):
	"""Generates the next state of the grid, replacing seats."""
	new_grid = copy.deepcopy(grid)
	cols = len(new_grid[1])
	rows = len(new_grid)
	changes = 0
	for j in range(rows):
		for i in range(cols):
			result = visible(i,j,grid)
			if grid[j][i] == '#':
				if result >= 5:
					changes += 1
					new_grid[j][i] = 'L'
				else:
					new_grid[j][i] = '#'
			elif grid[j][i] == 'L':
				if result == 0:
					changes += 1
					new_grid[j][i] = '#'
				else:
					new_grid[j][i] = 'L'
	return new_grid, changes

next_seats , changes = next_state(seats)
rounds = 1
while True:
	if changes == 0:
		break
	else:
		next_seats , changes = next_state(next_seats)
		print(f"Current changes: {changes} - round n° {rounds}")
		rounds += 1

total = 0
for x in next_seats:
	total += x.count('#')
print(f"Part two answer - occupied {total}")