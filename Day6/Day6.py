import os


def find_guard(lines: list[str]) -> tuple[int, int]:
    current_pos: tuple[int, int]
    for line_num in range(len(lines)):
        current_line = lines[line_num]
        if ("<" in current_line or "^" in current_line or ">" in current_line or "⌄" in current_line):
            for i in range(len(current_line)):
                if ("<" in current_line or "^" in current_line or
                        ">" in current_line or "⌄" in current_line):
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
    print(guard)
