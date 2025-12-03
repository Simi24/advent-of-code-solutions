import time

banks = []

def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
        for line in lines:
            banks.append(line.strip())

def get_largest_joltage_for_bank(bank: str) -> int:
    max_l = (0, 0)
    max_r = (0, 0)

    for i in range(len(bank) - 1):
        if max_l[0] < int(bank[i]):
            max_l = (int(bank[i]), i)
    
    for j in range(len(bank) - 1, max_l[1], -1):
        if max_r[0] < int(bank[j]):
            max_r = (int(bank[j]), j)
    return int(str(max_l[0]) + str(max_r[0]))


def solve_part1(banks: list[str]) -> int:
    output_joltage = 0
    for bank in banks:
        output_joltage += get_largest_joltage_for_bank(bank)
    
    return output_joltage

def get_largest_joltage_for_bank_2(bank: str) -> int:
    max_idx = -1
    max_joltage = ""
    activted_batteries = 12

    for i in range(activted_batteries):
        max_idx += 1
        max = bank[max_idx]
        offset = activted_batteries - i - 1
        for j in range(max_idx + 1, len(bank) - offset):
            if int(bank[j]) > int(max):
                max = bank[j]
                max_idx = j
        max_joltage += max
    return int(max_joltage)

def solve_part2(banks: list[str]) -> int:
    output_joltage = 0
    for bank in banks:
        output_joltage += get_largest_joltage_for_bank_2(bank)
    
    return output_joltage
    

if __name__ == "__main__":
    parseInput("input")

    start_time_part1 = time.perf_counter()
    print(solve_part1(banks))
    end_time_part1 = time.perf_counter()
    print(f"Part 1 executed in {end_time_part1 - start_time_part1:0.6f} seconds")

    start_time_part2 = time.perf_counter()
    print(solve_part2(banks))
    end_time_part2 = time.perf_counter()
    print(f"Part 2 executed in {end_time_part2 - start_time_part2:0.6f} seconds")