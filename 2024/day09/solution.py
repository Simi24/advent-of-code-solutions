blocks = []
occurrences = {}
spaces = {}
_line = ""


def parseInput():
    global _line
    with open("inputTest.txt") as file:
        lines = file.readlines()
        for line in lines:
            _line = line
            process_line(line)


def process_line(line):
    global blocks
    global occurrences
    global spaces

    index = 0
    indexSpaces = 0
    for i in range(len(line.strip())):
        if i % 2 == 0:
            n = int(line[i])
            while n > 0:
                blocks.append(index)
                n -= 1
            index += 1
        else:
            spaces[indexSpaces] = int(line[i])
            n = int(line[i])
            while n > 0:
                blocks.append(".")
                n -= 1
            indexSpaces += 1

    index = len(line) // 2
    for i in range(len(line) - 1, -1, -1):
        if i % 2 == 0:
            occurrences[index] = int(line[i])
            index -= 1


def reorderBlocks():
    l, r = 0, len(blocks) - 1

    while l < r:
        if blocks[r] == ".":
            r -= 1
        elif blocks[l] != "." and blocks[r] != ".":
            l += 1
        elif (blocks[l] != "." and blocks[r] == ".") or (
            blocks[l] == "." and blocks[r] != "."
        ):
            blocks[l], blocks[r] = blocks[r], blocks[l]
            l += 1
            r -= 1


def findChecksum():
    ret = 0

    for i in range(len(blocks)):
        if blocks[i] != ".":
            ret += blocks[i] * i

    return ret


def parse_disk_map(filename):
    with open(filename) as file:
        line = file.read().strip()

    disk_map = [int(x) for x in line]
    return disk_map


def compact_smart(disk_map):
    file_positions = []
    gap_positions = []
    current_position = 0

    for i, size in enumerate(disk_map):
        if i % 2 == 0:
            file_positions.append((i // 2, size, current_position))
        elif size > 0:
            gap_positions.append((size, current_position))
        current_position += size

    moved_files = []
    for file_id, size, position in reversed(file_positions):
        for i, (gap_size, gap_position) in enumerate(gap_positions):
            if gap_position > position:
                moved_files.append((file_id, size, position))
                break
            if gap_size < size:
                continue
            moved_files.append((file_id, size, gap_position))
            gap_positions[i] = (gap_size - size, gap_position + size)
            break
        else:
            moved_files.append((file_id, size, position))

    return moved_files


def smart_checksum(file_positions):
    return sum(
        file_id * (position * size + size * (size - 1) // 2)
        for file_id, size, position in file_positions
    )


def part1():
    parseInput()
    reorderBlocks()
    return findChecksum()


def part2(filename):
    disk_map = parse_disk_map(filename)
    moved_files = compact_smart(disk_map)
    return smart_checksum(moved_files)


def main():
    print("Part 1:", part1())
    print("Part 2:", part2("inputTest.txt"))


if __name__ == "__main__":
    main()
