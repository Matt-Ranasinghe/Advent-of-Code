import os


def create_dict_coords(lines: list[str]) -> dict[list[tuple[int, int]]]:
    coords_dict: dict[list[tuple[int, int]]] = {}
    line_num: int = 0
    for line in lines:
        for x, char in enumerate(line):
            coords_dict.setdefault(char, []).append((x + 1, line_num + 1))
        line_num += 1
    return coords_dict


if __name__ == "__main__":
    os.chdir("Day12")
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()
    coords_dict: dict[list[tuple[int, int]]] = create_dict_coords(lines)
    print(coords_dict["M"])
