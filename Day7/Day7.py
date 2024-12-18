import os


def get_numbers(lines: list[str]) -> tuple[list[int], list[list[int]]]:
    target: list[int] = []
    numbers_list: list[list[int]] = [[] for _ in range(len(lines))]
    target_and_numbers: list[str] = []
    for i in range(len(lines)):
        target_and_numbers = lines[i].split(":")
        target.append(int(target_and_numbers[0]))
        numbers_list[i] = list(map(int,
                                   (target_and_numbers[1].split(" "))[1:]))
    return (target, numbers_list)


def get_combinatoric_number(numbers: list[int]) -> int:
    # Permutations with repetition so takes the form 2^n
    return 2**(len(numbers) - 1)


def order_of_operations(determining_factor: int,
                        num_of_operations: int) -> list[int]:
    pos_of_mult: int = determining_factor
    mult_pos: list[int] = [0 for _ in range(num_of_operations)]
    for i in range(num_of_operations, 0, -1):
        if (pos_of_mult / (2**(i-1)) >= 1):
            pos_of_mult -= 2**(i-1)
            mult_pos[len(mult_pos) - i] = 1
    return mult_pos


def get_combinations(target: list[int], numbers_list: list[list[int]]) -> int:
    combinations: int
    operations: list[int]
    current_total: int
    valid_bridge: int = 0
    for i in range(len(numbers_list)):
        combinations = get_combinatoric_number(numbers_list[i])
        for x in range(combinations):
            current_total = numbers_list[i][0]
            operations = order_of_operations(x, len(numbers_list[i]) - 1)
            for w in range(len(operations)):
                if (operations[w] == 1):
                    current_total *= numbers_list[i][w+1]
                else:
                    current_total += numbers_list[i][w+1]
            if (current_total == target[i]):
                valid_bridge += target[i]
                break
    return valid_bridge


if __name__ == "__main__":
    os.chdir("Day7")
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()

    target, numbers_list = get_numbers(lines)
    print(get_combinations(target, numbers_list))