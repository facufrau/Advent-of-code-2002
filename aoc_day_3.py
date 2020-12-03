# --- Day 3: Toboggan Trajectory ---
# by Facundo Frau - Github facufrau

def calculate_trees(lines_list, right, down):
    """
    Calculate the number of trees in a path with a slope (right-down)
    """
    trees = 0  # Trees are marked '#' in lines, '.' for open squares.
    row = 0  # Row for iterating over lines
    block = 0  # Row for iterating along each line.
    row_length = len(lines_list[0])

    while row < len(lines_list) - 1:
        row += down
        block += right
        if block > row_length - 1:
            block = block % row_length
            if lines_list[row][block] == '#':
                trees += 1
        else:
            if lines_list[row][block] == '#':
                trees += 1
    return trees

# Open and read input for both parts.
with open('day3_input.txt','r') as f:
    lines = f.read().splitlines()

# Part one.
trees = calculate_trees(lines, 3, 1)
print(f"Part 1 answer - N° Trees: {trees}")

# Part two.
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
result = 1
for slope in slopes:
    result *= calculate_trees(lines, slope[0], slope[1])
print(f"Part 2 answer - N° Trees multiplied for all cases: {result}")