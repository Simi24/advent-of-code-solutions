from collections import defaultdict

stones = []


def parseInput():
    with open("input.txt") as file:
        for line in file:
            stones.extend([int(x) for x in line.strip().split()])

        print(stones)


def stonesAfterNSeconds(n):
    global stones
    stone_count = defaultdict(int)
    for stone in stones:
        stone_count[stone] += 1

    for _ in range(n):
        new_stone_count = defaultdict(int)
        for stone, count in stone_count.items():
            if stone == 0:
                new_stone_count[1] += count
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                left = int(str(stone)[:half])
                right = int(str(stone)[half:])
                new_stone_count[left] += count
                new_stone_count[right] += count
            else:
                new_stone_count[stone * 2024] += count
        stone_count = new_stone_count

    tot_count = sum(stone_count.values())

    print(tot_count)
    return tot_count


def main():
    global stones
    parseInput()
    stonesAfterNSeconds(75)


if __name__ == "__main__":
    main()
