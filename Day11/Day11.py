import os


def rock_logic(rocks: list[int]) -> list[int]:
    num_of_rocks: int = len(rocks)
    i: int = 0
    while (i < num_of_rocks):
        if (rocks[i] == 0):
            rocks[i] = 1
        elif (len(str(rocks[i])) % 2 == 0):
            rocks.insert(i+1, int(str(rocks[i])[int(len(str(rocks[i]))/2):]))
            rocks[i] = int(str(rocks[i])[:int(len(str(rocks[i]))/2)])
            i += 1  # ignores rock for this cycle
            num_of_rocks += 1
        else:
            rocks[i] *= 2024
        i += 1
    return rocks


if __name__ == "__main__":
    os.chdir("Day11")
    with open("input.txt", "r") as file:
        line: str = file.read()
    rocks: list[int] = list(map(int, line.split(" ")))
    for _ in range(25):
        rocks = rock_logic(rocks)
    print(len(rocks))
