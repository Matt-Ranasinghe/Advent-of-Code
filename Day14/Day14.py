import os
import re


def data_extract(lines_data: list[tuple[str, str]]
                 ) -> tuple[list[list[int]], list[tuple[int, int]]]:
    start_points: list[list[int]] = []
    velocities: list[tuple[int, int]] = []
    data_str: list[tuple[str, str]] = []
    for data_point in lines_data:
        for i in range(2):
            data_str.append(
                "".join(re.findall("-?\d+,-?\d+", data_point[i])).split(","))
        start_points.append([int(data_str[0][0]), int(data_str[0][1])])
        velocities.append((int(data_str[1][0]), int(data_str[1][1])))
        data_str = []
    return (start_points, velocities)


def create_grid() -> list[list[int]]:
    grid: list[list[int]] = [[0 for _ in range(101)] for _ in range(103)]
    return grid


def robot_move(robot_positions: list[list[int]],
               velocities: list[tuple[int, int]]) -> list[list[int]]:
    for i in range(len(robot_positions)):
        for x in range(2):
            robot_positions[i][x] += velocities[i][x]
            match x % 2:
                case 0:
                    robot_positions[i][x] = robot_positions[i][x] % 101
                    if (robot_positions[i][x] < 0):
                        robot_positions[i][x] += 101
                case _:
                    robot_positions[i][x] = robot_positions[i][x] % 103
                    if (robot_positions[i][x] < 0):
                        robot_positions[i][x] += 103
    return robot_positions


def populate_grid(robot_positions: list[list[int]]) -> list[list[int]]:
    grid: list[list[int]] = create_grid()
    count: int = 0
    for position in robot_positions:
        grid[position[1]][position[0]] += 1
        print(count)
        count += 1
    return grid


def calulate_safety(grid: list[list[int]]) -> int:
    counter: int = 0
    grid_safety: list[int] = [0, 0, 0, 0]
    safety: int = 1
    for row in grid:
        if (counter < 51):
            for i in range(len(row)):
                if (i < 50):
                    grid_safety[0] += row[i]
                elif (i > 50):
                    grid_safety[1] += row[i]
        elif (counter > 51):
            for i in range(len(row)):
                if (i < 50):
                    grid_safety[2] += row[i]
                elif (i > 50):
                    grid_safety[3] += row[i]
        counter += 1
    for num in grid_safety:
        safety *= num
    return safety


if __name__ == "__main__":
    os.chdir("Day14")
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()
    lines_data: list[tuple[str, str]] = [tuple(line.split(" "))
                                         for line in lines]
    robot_pos: list[list[int]]
    velocities: list[tuple[int, int]]
    robot_positions, velocities = data_extract(lines_data)
    for i in range(100):
        robot_positions = robot_move(robot_positions, velocities)
    grid: list[list[int]] = populate_grid(robot_positions)
    for line in grid:
        print(line)
    print(calulate_safety(grid))
