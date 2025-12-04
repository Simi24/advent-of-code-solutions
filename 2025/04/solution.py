import time

grid = []

def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(line.strip()))

def solve_part1(grid: list[str]) -> int:
    accessed_rolls_paper = 0
    ROWS, COLS = len(grid), len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    for r in range(ROWS):
        for c in range(COLS):
            cell = grid[r][c]
            if cell != '@':
                continue
            adjacent_rolls_paper = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    neighbor = grid[nr][nc]
                    if neighbor == '@':
                        adjacent_rolls_paper += 1
            if adjacent_rolls_paper < 4:
                accessed_rolls_paper += 1
    return accessed_rolls_paper

def solve_part2(grid: list[str]) -> int:
    accessed_rolls_paper = 0
    ROWS, COLS = len(grid), len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    coordinate_accessed_rolls = set((0,0))
    while coordinate_accessed_rolls:
        coordinate_accessed_rolls.clear()
        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]
                if cell != '@':
                    continue
                adjacent_rolls_paper = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        neighbor = grid[nr][nc]
                        if neighbor == '@':
                            adjacent_rolls_paper += 1
                if adjacent_rolls_paper < 4:
                    accessed_rolls_paper += 1
                    coordinate_accessed_rolls.add((r, c))
        for r, c in coordinate_accessed_rolls:
            grid[r][c] = 'X'
    return accessed_rolls_paper

if __name__ == "__main__":
    parseInput("input")

    start_time_part1 = time.perf_counter()
    print(solve_part1(grid))
    end_time_part1 = time.perf_counter()
    print(f"Part 1 executed in {end_time_part1 - start_time_part1:0.6f} seconds")

    start_time_part2 = time.perf_counter()
    print(solve_part2(grid))
    end_time_part2 = time.perf_counter()
    print(f"Part 2 executed in {end_time_part2 - start_time_part2:0.6f} seconds")