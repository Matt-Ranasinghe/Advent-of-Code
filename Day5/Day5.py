from math import floor
import os

os.chdir("Day5")
with open("input.txt", "r") as file:
    update_rules: list[str] = file.read().splitlines()

rules_table: list[list[int]] = [[] for _ in range(100)]
print(len(rules_table))
print(rules_table[0])
split_line: list[int] = []
for line in update_rules:
    split_line = list(map(int, str(line).split("|")))
    rules_table[split_line[0]].append(split_line[1])

with open("input_2.txt", "r") as file:
    manuals: list[str] = file.read().splitlines()

sum: int = 0
for manual in manuals:
    pages: list[int] = list(map(int, manual.split(",")))
    invalid_prints: list[int] = []
    for i in range(len(pages) - 1, -1, -1):
        if (pages[i] in invalid_prints):
            break
        elif (i == 0):
            sum += pages[floor(len(pages)/2)]
        else:
            for x in rules_table[pages[i]]:
                invalid_prints.append(x)
print(sum)