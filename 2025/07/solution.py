from collections import deque
from functools import cache

matrix1 = []
matrix2 = []

def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
        for line in lines:
            matrix1.append(list(line.strip()))
            matrix2.append(list(line.strip()))

def find_starting_position(matrix: list[list[str]]) -> tuple[int, int]:
    ROWS, COLS = len(matrix), len(matrix[0])

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 'S':
                return (r, c)

def solve_part1(matrix: list[list[str]]):
    ROWS, COLS = len(matrix), len(matrix[0])
    start = find_starting_position(matrix)
    splits = 0
    q = deque()
    q.append(start)
    
    while q:
        r, c = q.popleft()
        if r + 1 > ROWS:
            break
        splitted = False

        if matrix[r][c] == '^':
            if c-1 >= 0 and matrix[r][c-1] == ".":
                q.append((r, c-1))
                matrix[r][c-1] = "|"
                splitted = True
                q.append((r+1, c-1))
            
            if c+1 <= COLS and matrix[r][c+1] == ".":
                q.append((r, c+1))
                matrix[r][c+1] = "|"
                splitted = True
                q.append((r+1, c+1))
            if splitted:
                splits += 1

        else: 
            q.append((r+1, c))
            matrix[r][c] = "|"
        
    print(splits)

def solve_part2(matrix: list[list[str]]):
    ROWS, COLS = len(matrix), len(matrix[0])
    start = find_starting_position(matrix)

    @cache
    def dfs(r: int, c: int) -> int:
        if r == ROWS:
            return 1
        if r > ROWS or c >= COLS or c < 0:
            return 0
        
        count = 0
        
        if matrix[r][c] == '^':
            count += dfs(r, c-1)
            count += dfs(r, c+1)

        else: 
            count += dfs(r+1, c)
        
        return count
        
    print(dfs(start[0], start[1]))

    


if __name__ == "__main__":
    parseInput("test")
    solve_part1(matrix1)
    solve_part2(matrix2)