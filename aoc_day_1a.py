from itertools import permutations

with open ('day1a_input.txt', 'r') as f:
    report = [int(x) for x in f.readlines()]

# Test case -> answer 514579
# report = [1721, 979, 366, 299, 675, 1456]

def check_report(num_lst):
    """
    Check for two numbers that add up 2020 and return their product.
    """
    for i in range(len(num_lst)):
        for j in range(i + 1):
            entry_1 = num_lst[i]
            entry_2 = num_lst[j]
            if entry_1 + entry_2 == 2020:
                return entry_1 * entry_2

answer = check_report(report)
print(answer)

perm = list(permutations(report, r=3))
for p in perm:
    check = p[0] + p[1] + p[2]
    if check == 2020:
        answer_2 = p[0] * p[1] * p[2]
        break

print(answer_2)