import os


def find_guard(lines: list[str]) -> tuple[int, int]:
    current_pos: tuple[int, int]
    for line_num in range(len(lines)):
        current_line = lines[line_num]
        if ("<" in current_line or "^" in current_line or
                ">" in current_line or "⌄" in current_line):
            for i in range(len(current_line)):
                if ("<" == current_line[i] or "^" == current_line[i] or
                        ">" == current_line[i] or "⌄" == current_line[i]):
                    # Representing in the form x,y
                    current_pos = (i, line_num)
                    return current_pos


if __name__ == "__main__":
    os.chdir("Day6")

    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()
    
    position: tuple[int, int] = find_guard(lines)
    direction: str = lines[position[1]][position[0]]
    guard: dict[str, str | int] = {"x": position[0],
                                   "y": position[1],
                                   "direction": direction}
    movement_count: int = 1
    lines_list: list[list[str]] = [[char for char in line] for line in lines]
    visited: list[tuple[int, int]] = [(guard["x"], guard["y"])]
    while (True):
        match guard["direction"]:
            case "^":
                if (guard["y"] < 1):
                    break
                elif (lines_list[guard["y"] - 1][guard["x"]] == "#"):
                    guard["direction"] = ">"
                else:
                    guard["y"] -= 1
                    if ((guard["x"], guard["y"]) not in visited):
                        movement_count += 1
                        visited.append((guard["x"], guard["y"]))
            case ">":
                if (guard["x"] == len(lines_list[0]) - 1):
                    break
                elif (lines_list[guard["y"]][guard["x"] + 1] == "#"):
                    guard["direction"] = "⌄"
                else:
                    guard["x"] += 1
                    if ((guard["x"], guard["y"]) not in visited):
                        movement_count += 1
                        visited.append((guard["x"], guard["y"]))
            case "⌄":
                if (guard["y"] == len(lines_list) - 1):
                    break
                elif (lines_list[guard["y"] + 1][guard["x"]] == "#"):
                    guard["direction"] = "<"
                else:
                    guard["y"] += 1
                    if ((guard["x"], guard["y"]) not in visited):
                        movement_count += 1
                        visited.append((guard["x"], guard["y"]))
            case _:
                if (guard["x"] < 1):
                    break
                elif (lines_list[guard["y"]][guard["x"] - 1] == "#"):
                    guard["direction"] = "^"
                else:
                    guard["x"] -= 1
                    if ((guard["x"], guard["y"]) not in visited):
                        movement_count += 1
                        visited.append((guard["x"], guard["y"]))
        lines_list[guard["y"]][guard["x"]] = guard["direction"]
    print(movement_count)