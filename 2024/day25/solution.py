locks = []
keys = []


def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()
        matrix = []
        for line in lines:

            if line == "\n":
                if matrix[0][0] == "#":
                    locks.append(matrix)
                else:
                    keys.append(matrix)

                matrix = []
                continue
            else:
                matrix.append(line.strip())
            if line == lines[-1]:
                if matrix[0][0] == "#":
                    locks.append(matrix)
                else:
                    keys.append(matrix)


def find_heights_of_locks(lock):
    heights = [0 for _ in range(len(lock[0]))]
    for y in range(len(lock)):
        if y == 0:
            continue
        for x in range(len(lock[y])):
            if lock[y][x] == "#":
                heights[x] += 1
    return heights


def find_heights_of_keys(key):
    heights = [0 for _ in range(len(key[0]))]
    for y in range(len(key)):
        if y == 0 or y == len(key) - 1:
            continue
        for x in range(len(key[y])):
            if key[y][x] == "#":
                heights[x] += 1
    return heights


def does_key_fit(lock, key):
    for y in range(len(lock)):
        for x in range(len(lock[y])):
            if key[y][x] == "#" and lock[y][x] == "#":
                return False
    return True


def main():
    parse_input()
    ret = 0
    for lock in locks:
        for key in keys:
            if does_key_fit(lock, key):
                ret += 1
    print(ret)


if __name__ == "__main__":
    main()
