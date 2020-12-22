# --- Day 6: Custom Customs ---
# by Facundo Frau - Github facufrau

# Part one.
answers = 0
current = set()
with open('day6_input.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        if line == '':
            answers += len(current)
            current = set()
        else:
            current = set(line) | current
print(f"Part 1 answer - N° yes answers: {answers}")

# Part two.
answers = 0
group = []
with open('day6_input.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        if line == '':
            # Idea for this line from: https://stackoverflow.com/a/2541814
            answers += len(set.intersection(*group))
            group = []
        else:
            group.append(set(line))
print(f"Part 2 answer - N° yes answers: {answers}")