import os
import re
os.chdir("Day3")

with open("input.txt", "r") as file:
    lines: str = file.read()
    mul: list[str] = re.findall("mul\(\d+,\d+\)", lines)
    digits: list[int] = [re.findall("\d+", i) for i in mul]
    sum: int = 0
    for i in digits:
        sum += int(i[0])*int(i[1])
print(sum)