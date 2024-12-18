import os


if __name__ == "__main__":
    os.chdir("Day13")
    with open("input.txt", "r") as file:
        lines: list[str] = file.read().splitlines()
    lines = [line for line in lines if line.strip()]
    print(lines)