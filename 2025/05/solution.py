from platform import java_ver
import time

prod_ranges = []
available_ids = []

def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
        for line in lines:
            if "-" in line:
                parts = line.strip().split("-")
                start, end = int(parts[0]), int(parts[1])
                prod_ranges.append((start, end))
            elif line != "\n":
                line.strip()
                available_ids.append(int(line))

def solve_part1(prod_ranges: list[tuple[int, int]], available_ids: list[int]):
    fresh_ingredients = []
    for id in available_ids:
        for start, end in prod_ranges:
            if start <= id <= end:
                fresh_ingredients.append(id)
                break
    print(f"Part 1: Number of fresh ingredients available: {len(fresh_ingredients)}")

def rearrange_prod_ranges(prod_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:

    def isRangeContained(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
        start1, end1 = range1[0], range1[1]
        start2, end2 = range2[0], range2[1]
        return start1 >= start2 and end1 <= end2

    def doesRangeContains(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
        start1, end1 = range1[0], range1[1]
        start2, end2 = range2[0], range2[1]
        return start1 <= start2 and end1 >= end2
    
    def isRangeLeftOverlapping(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
        start1, end1 = range1[0], range1[1]
        start2, end2 = range2[0], range2[1]
        return start1 <= start2 and end1 <= end2 and end1 >= start2
    
    def isRangeRightOverlapping(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
        start1, end1 = range1[0], range1[1]
        start2, end2 = range2[0], range2[1]
        return start1 >= start2 and end1 >= end2 and start1 <= end2
    
    final_prod_ranges = []
    while prod_ranges:
        current_range = prod_ranges.pop(0)
        has_merged = False
        for i in range(len(prod_ranges)):
            compare_range = prod_ranges[i]
            if isRangeContained(current_range, compare_range):
                current_range = compare_range
                prod_ranges.pop(i)
                has_merged = True
                break
            elif doesRangeContains(current_range, compare_range):
                prod_ranges.pop(i)
                has_merged = True
                break
            elif isRangeLeftOverlapping(current_range, compare_range):
                current_range = (current_range[0], compare_range[1])
                prod_ranges.pop(i)
                has_merged = True
                break
            elif isRangeRightOverlapping(current_range, compare_range):
                current_range = (compare_range[0], current_range[1])
                prod_ranges.pop(i)
                has_merged = True
                break
        if not has_merged:
            final_prod_ranges.append(current_range)
        else:
            prod_ranges.append(current_range)
    return final_prod_ranges

def solve_part2(prod_ranges: list[tuple[int, int]]):
    final_prod_ranges = rearrange_prod_ranges(prod_ranges)
    fresh_ingredients = 0
    for start, end in final_prod_ranges:
        fresh_range = end - start + 1
        fresh_ingredients += fresh_range
    
    print(f"Part 2: Number of range fresh ingredient available: {fresh_ingredients}")


if __name__ == "__main__":
    parseInput("input")
    start_time_part1 = time.perf_counter()
    solve_part1(prod_ranges, available_ids)
    end_time_part1 = time.perf_counter()
    elapsed_time_part1 = end_time_part1 - start_time_part1
    print(f"Part 1 execution time: {elapsed_time_part1:.6f} s")

    start_time_part2 = time.perf_counter()
    solve_part2(prod_ranges)
    end_time_part2 = time.perf_counter()
    elapsed_time_part2 = end_time_part2 - start_time_part2
    print(f"Part 2 execution time: {elapsed_time_part2:.6f} s")