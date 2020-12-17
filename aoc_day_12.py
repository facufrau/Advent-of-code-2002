# --- Day 12: Rain Risk ---
# by Facundo Frau - Github facufrau
with open('day12_input.txt') as f:
    instructions = [[x[0], int(x[1:])] for x in f.read().splitlines()]

# Part one.
class Ship():
    def __init__(self):
        self.facing = 'E'
        self.coord_x = 0
        self.coord_y = 0

    def move(self, direction, number):
        """
        Moves the ship {number} units in {direction}
        """
        if direction == 'N':
            self.coord_y += number
        elif direction == 'S':
            self.coord_y -= number
        elif direction == 'E':
            self.coord_x += number
        elif direction == 'W':
            self.coord_x -= number
    
    def rotate(self, turn, amount):
        """
        Rotates the ship in {turn} direction {amount} degrees
        """
        to_angles = {'N': 90, 'S': 270, 'E': 0, 'W': 180}
        to_facing = {90: 'N', 270: 'S', 0: 'E', 180: 'W'}
        if turn == 'R':
            angle = (to_angles[self.facing] - amount) % 360
            self.facing = to_facing[angle]
        elif turn == 'L':
            angle = (to_angles[self.facing] + amount) % 360
            self.facing = to_facing[angle]

my_ship = Ship()
for order in instructions:
    action = order[0]
    value = order[1]
    if action == 'F':
        my_ship.move(my_ship.facing, value)
    elif action in ['R', 'L']:
        my_ship.rotate(action, value)
    elif action in ['N', 'S', 'E', 'W']:
            my_ship.move(action, value)
    #print(f"FACING: {my_ship.facing} - COORD X: {my_ship.coord_x} - COORD Y:{my_ship.coord_y}")
answer_1 = abs(my_ship.coord_x) + abs(my_ship.coord_y)
print(f"Part 1 - Manhattan Dist: {answer_1}")