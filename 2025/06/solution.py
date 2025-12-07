import math
from functools import reduce
import operator
import re

problems_matrix = []
problem_matrix2 = []

def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        # lines = file.readlines()
        for line in file:
            problems_matrix.append([x for x in line.strip().split()])

def parse_part2(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    cols = []
    for x in range(max_len):
        col = [line[x] for line in padded_lines]
        cols.append(col)
        
    blocks = []
    current_block = []
    
    for col in cols:
        if all(c == ' ' for c in col):
            if current_block:
                blocks.append(current_block)
                current_block = []
        else:
            current_block.append(col)
            
    if current_block:
        blocks.append(current_block)
        
    parsed_problems = []
    for block in blocks:
        nums = []
        op = None
        
        for col in block:
            if col[-1] in "*+":
                op = col[-1]
                
        for col in block:
            digits = col[:-1]
            num_str = "".join(digits).replace(" ", "")
            if num_str:
                nums.append(int(num_str))
                
        if op and nums:
            parsed_problems.append((nums, op))
            
    all_values = [p[0] for p in parsed_problems]
    all_ops = [p[1] for p in parsed_problems]
    
    return all_values, all_ops

def solve_part1(problems_matrix: list[list[str]]):
    tot_sum = 0
    ROWS, COLS = len(problems_matrix), len(problems_matrix[0])
    for c in range(COLS):
        colum = []
        operation = ""
        for r in range(ROWS):
            if problems_matrix[r][c].isalnum():
                colum.append(int(problems_matrix[r][c]))
            else:
                operation = problems_matrix[r][c]
        print(colum, operation)
        if operation == "*":
            tot_sum += math.prod(colum) 
        elif operation == "+":
            tot_sum += sum(colum)

    print(tot_sum)

def compute(data: tuple[list[list[int]], list[str]]) -> int:
    total = 0
    for values, op in zip(*data, strict=True):
        if op == "*":
            total += reduce(operator.mul, values)
        else:
            total += reduce(operator.add, values)
    return total

if __name__ == "__main__":
    print("Test Part 2:", compute(parse_part2("test")))
    print("Input Part 2:", compute(parse_part2("input")))
