import os


def find_as(lines: list[str],
            coord: tuple[int, int],
            direction: str,
            character: str) -> int:
    x: int = coord[0]
    y: int = coord[1]
    if "U" in direction:
        y -= 1
    elif "D" in direction:
        y += 1
    if "L" in direction:
        x -= 1
    elif "R" in direction:
        x += 1
    if (x < 0 or x == len(lines[0]) or y < 0 or y == len(lines)):
        return 0
    if (lines[y][x] == character):
        if (character == "S"):
            return 1
        else:
            return find_as(lines, (x, y), direction, "S")
    return 0


def find_m(lines: list[str], x: int, y: int) -> int:
    queue_of_coords: list[tuple[int, int]] = []
    orientation = ""
    directions: list[str] = []
    sum: int = 0
    for i in range(y - 1, y + 2):
        if (i == len(lines)):
            break
        elif (i >= 0):
            for j in range(x - 1, x + 2):
                if (j == len(lines[0])):
                    break
                elif (j >= 0):
                    if (lines[i][j] == "M"):
                        if (i < y):
                            orientation = orientation + "U"
                        elif (i > y):
                            orientation = orientation + "D"
                        if (j < x):
                            orientation = orientation + "L"
                        elif (j > x):
                            orientation = orientation + "R"
                        queue_of_coords.append((j, i))
                        directions.append(orientation)
                        orientation = ""
    while (queue_of_coords != []):
        coord = queue_of_coords.pop(0)
        direction = directions.pop(0)
        sum += find_as(lines, coord, direction, "A")
    return sum


def find_x(lines: list[str]) -> int:
    total: int = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (lines[y][x] == "X"):
                total += find_m(lines, x, y)
    return total


if __name__ == "__main__":
    os.chdir("Day4")
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()
    total: int = 0
    total += find_x(lines)
    print(total)
