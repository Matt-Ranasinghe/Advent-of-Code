import os


def build_memory_disk(line: str) -> list[str]:
    memory_disk: str = ""
    empty_space: bool = False
    for i in range(len(line)):
        if (empty_space):
            memory_disk = memory_disk + ("."*int(line[i]))
        else:
            memory_disk = memory_disk + (str(int(i/2))*int(line[i]))
        empty_space = not empty_space
    return list(memory_disk)


def minimise_memory(disk: list[str]) -> str:

    reformatted_disk: str = ""
    current_mem_length: int = len(disk)
    i: int = 0
    while (i < current_mem_length):
        if (disk[i] == "."):
            for x in range(len(disk) - 1, i, -1):
                if (disk[x] != "."):
                    disk[i] = disk.pop(x)
                    current_mem_length -= 1
                    break
                else:
                    disk.pop(x)
                    current_mem_length -= 1
            i += 1
    reformatted_disk: str = "".join(disk)
    return reformatted_disk


def calculate_check_sum(reformatted_disk: str) -> int:
    check_sum: int = 0
    for i in range(len(reformatted_disk)):
        check_sum += int(reformatted_disk[i])*i
    return check_sum


if __name__ == "__main__":
    os.chdir("Day9")

    with open("input.txt", "r") as file:
        line: str = file.read()
    
    disk: list[str] = build_memory_disk(line)
    reformatted_disk: str = minimise_memory(disk)
    check_sum: int = calculate_check_sum(reformatted_disk)
    print(check_sum)