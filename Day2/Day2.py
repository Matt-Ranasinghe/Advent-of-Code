import os

os.chdir("Day2")

with open("input.txt", "r") as file:
    lines: list[str] = file.readlines()
    digit_list: list[int]
    increasing: bool
    temp_list: list[int] = []
    sum_of_safe: int = 0
    for line in lines:
        digit_list = list(map(int, line.strip().split(" ")))
        for i in range(len(digit_list) - 1):
            if (i == 0):
                if (digit_list[i] < digit_list[i+1]):
                    increasing = True
                else:
                    increasing = False
            if (increasing and digit_list[i] > digit_list[i+1]):
                break
            elif (not increasing and digit_list[i] < digit_list[i+1]):
                break
            elif (abs(digit_list[i] - digit_list[i+1]) > 3 or
                  abs(digit_list[i] - digit_list[i+1]) == 0):
                break
            if (i == len(digit_list) - 2):
                sum_of_safe += 1
print(sum_of_safe)
