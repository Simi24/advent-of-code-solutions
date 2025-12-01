rotation_sequence = []
starting_position = current_position = 50
zeros_count = 0

def parseInput(file_name: str = "input"):
    with open(file_name+".txt") as file:
        lines = file.readlines()
        for line in lines:
            rotation_sequence.append(line.strip())

def rotate_left(pos: int, steps: int) -> tuple[int, int]:
    zeros_count = 0
    for _ in range(steps):
        zeros_count = zeros_count + 1 if pos == 0 else zeros_count
        pos = 99 if pos == 0 else pos - 1
    
    return (pos, zeros_count)

def rotate_right(pos: int, steps: int) -> tuple[int, int]:
    zeros_count = 0
    for _ in range(steps):
        zeros_count = zeros_count + 1 if pos == 0 else zeros_count
        pos = 0 if pos == 99 else pos + 1
    return (pos, zeros_count)

def solve_part1(rotation_sequence: list[str]) -> int:
    current_position = starting_position
    zeros_count = 0
    for rotation in rotation_sequence:
        match rotation[0]:
            case 'L':
                current_position = (current_position - int(rotation[1:])) % 100
                if current_position == 0:
                    zeros_count += 1
            case 'R':
                current_position = (current_position + int(rotation[1:])) % 100
                if current_position == 0:
                    zeros_count += 1
    
    print("Zeros positions: ", zeros_count)

def solve_part2(rotation_sequence: list[str]) -> int:
    current_position = starting_position
    zeros_count = 0
    for rotation in rotation_sequence:
        match rotation[0]:
            case 'L':
                current_position, local_zeros = rotate_left(current_position, int(rotation[1:]))
                zeros_count += local_zeros
            case 'R':
                current_position, local_zeros = rotate_right(current_position, int(rotation[1:]))
                zeros_count += local_zeros
    
    print("Zeros positions: ", zeros_count)

if __name__ == "__main__":
    parseInput("input")
    solve_part1(rotation_sequence)
    solve_part2(rotation_sequence)