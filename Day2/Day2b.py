import os

os.chdir("Day2")

with open("input.txt", "r") as file:
    lines = [[int(i) for i in line.split()] for line in file.read().splitlines()]

count = 0
for line in lines:
    diffs = [(line[i+1]-line[i]) for i in range(len(line[:-1]))]

    increasing = [i>0 for i in diffs]
    decreasing = [i<0 for i in diffs]
    gaps = [1<=abs(i)<=3 for i in diffs]

    if (all(increasing) or all(decreasing)) and all(gaps):
        count += 1
    else:
        for j, x in enumerate(line):
            tmp_line = line.copy()
            tmp_line.pop(j)
            tmp_diffs = [(tmp_line[i+1]-tmp_line[i]) for i in range(len(tmp_line[:-1]))]
            tmp_increasing = [i>0 for i in tmp_diffs]
            tmp_decreasing = [i<0 for i in tmp_diffs]
            tmp_gaps = [1<=abs(i)<=3 for i in tmp_diffs]
            if (all(tmp_increasing) or all(tmp_decreasing)) and all(tmp_gaps):
                count += 1
                break

print(count)