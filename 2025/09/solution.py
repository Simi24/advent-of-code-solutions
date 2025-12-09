import math

coordinates: list[tuple[int, int]] = []

def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
        for line in lines:
            coordinates.append(tuple(int(x) for x in line.strip().split(",")))

def get_area(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (abs(b[0] - a[0])+1) * (abs(b[1] - a[1])+1)

def solve_part1(coordinates: list[tuple[int, int]]):
    max_area = 0
    for i in range(len(coordinates) -1):
        for j in range(i + 1, len(coordinates)):
            area = get_area(coordinates[i], coordinates[j])
            max_area = max(max_area, area)
    
    print(max_area)

if __name__ == "__main__":
    parseInput("input")
    solve_part1(coordinates)
