import os
import re
os.chdir("Day3")

with open("input.txt", "r") as file:
    one_line: str = file.read()
    lines: list[str] = one_line.split("\n")
    split_do: list[str] = [line.split("do()") for line in lines]
    split_line: list[str]
    sum: int = 0
    for line in split_do:
        split_line = str(line).split("don't")
        for i in range(1, len(split_line), 2):
            mul = re.findall("mul\(\d+,\d+\)", str(split_line[i]))
            digits: list[str] = [re.findall("\d+", i) for i in mul]
        for i in digits:
            sum += int(i[0])*int(i[1])
print(sum)