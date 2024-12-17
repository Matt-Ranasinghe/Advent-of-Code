import os
os.chdir("Day8")


def create_dict_of_antenna(lines: list[str]
                           ) -> dict[str, list[tuple[int, int]]]:
    antenna_coords: dict[str, list[tuple[int, int]]] = {}
    line_num: int = 0
    for line in lines:
        for i, char in enumerate(line):
            if (char != "."):
                """
                Appending the coordinates in form x,y;
                rather than row, column.
                """
                antenna_coords.setdefault(char, []).append(
                    (i + 1, line_num + 1))
        line_num += 1
    return antenna_coords


def get_dimensions(lines: list[str]) -> tuple[int, int]:
    return ((len(lines[0]), len(lines)))


def in_bounds(dimensions: tuple[int, int],
              first_coord: tuple[int, int],
              second_coord: tuple[int, int]) -> list[tuple[int, int]]:
    sub_from_first: bool = False
    valid_anti_nodes: list[tuple[int, int]] = []
    if (first_coord[0] < second_coord[0]):
        sub_from_first = True
    move_coords = (abs(first_coord[0] - second_coord[0]),
                   abs(first_coord[1] - second_coord[1]))
    match sub_from_first:
        case True:
            if (not (first_coord[0] - move_coords[0] <= 0 or
                     first_coord[1] - move_coords[1] <= 0)):
                valid_anti_nodes.append((first_coord[0] - move_coords[0],
                                         first_coord[1] - move_coords[1]))
            if (not (second_coord[0] + move_coords[0] > dimensions[0] or
                     second_coord[1] + move_coords[1] > dimensions[1])):
                valid_anti_nodes.append((second_coord[0] + move_coords[0],
                                         second_coord[1] + move_coords[1]))
        case False:
            if (not (first_coord[0] + move_coords[0] > dimensions[0] or
                     first_coord[1] - move_coords[1] <= 0)):
                valid_anti_nodes.append((first_coord[0] + move_coords[0],
                                         first_coord[1] - move_coords[1]))
            if (not (second_coord[0] - move_coords[0] < 0 or
                     second_coord[1] + move_coords[1] > dimensions[1])):
                valid_anti_nodes.append((second_coord[0] - move_coords[0],
                                         second_coord[1] + move_coords[1]))
    return valid_anti_nodes


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()
    
    antennas: dict[str, list[tuple[int, int]]] = create_dict_of_antenna(lines)
    dimensions: tuple[int, int] = get_dimensions(lines)
    valid_anti_nodes: list[tuple[int, int]] = []
    for coord_lists in antennas.values():
        for i in range(len(coord_lists) - 1):
            for x in range(1 + i, len(coord_lists)):
                anti_nodes: list[tuple[int, int]] = in_bounds(dimensions,
                                                              coord_lists[i],
                                                              coord_lists[x])
                for w in anti_nodes:
                    if (w not in valid_anti_nodes and w is not None):
                        valid_anti_nodes.append(w)
    print(len(valid_anti_nodes))