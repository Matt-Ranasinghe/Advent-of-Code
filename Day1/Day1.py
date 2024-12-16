import os

os.chdir("Day1")    

with open("input.txt", "r") as file:
    lines = file.readlines()
    list1: list[int] = []
    list2: list[int] = []
    for line in lines:
        distances: list[int] = list(map(int, line.strip().split("  ")))
        list1.append(distances[0])
        list2.append(distances[1])
    list1.sort()
    list2.sort()
    sum: int = 0
    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])
print(sum)