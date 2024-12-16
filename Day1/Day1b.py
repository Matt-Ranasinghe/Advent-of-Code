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
    num_of_appearances: list[int] = [0]*100000
    for i in range(1, len(list2)):
        num_of_appearances[list2[i]] += 1
    sum: int = 0
    for i in range(len(list1)):
        sum += list1[i] * num_of_appearances[list1[i]]
print(sum)