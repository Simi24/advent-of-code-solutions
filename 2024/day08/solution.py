from typing import List
import math

grid = []

frequencyMap = {}


def parseInput():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            grid.append(row)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == ".":
                    continue
                if grid[i][j] in frequencyMap:
                    frequencyMap[grid[i][j]].append((i, j))
                else:
                    frequencyMap[grid[i][j]] = [(i, j)]


def findNumberOfAntinodes():
    antinodes = 0
    antinodesMap = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for key in frequencyMap:
        if len(frequencyMap[key]) > 1:
            for i in range(len(frequencyMap[key])):
                antinodes += 1
                n1 = frequencyMap[key][i]
                for j in range(i + 1, len(frequencyMap[key])):
                    n2 = frequencyMap[key][j]
                    distance = math.sqrt((n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2)
                    dx = (n2[0] - n1[0]) / distance
                    dy = (n2[1] - n1[1]) / distance

                    a1 = (round(n1[0] - dx * distance), round(n1[1] - dy * distance))
                    a2 = (round(n2[0] + dx * distance), round(n2[1] + dy * distance))

                    # Part 1
                    # if (a1[0] >= 0 and a1[0] < len(grid)) and (a1[1] >= 0 and a1[1] < len(grid[0])):
                    #     if antinodesMap[a1[0]][a1[1]] == False:
                    #         antinodesMap[a1[0]][a1[1]] = True
                    #         antinodes += 1
                    # if (a2[0] >= 0 and a2[0] < len(grid)) and (a2[1] >= 0 and a2[1] < len(grid[0])):
                    #     if antinodesMap[a2[0]][a2[1]] == False:
                    #         antinodesMap[a2[0]][a2[1]] = True
                    #         antinodes += 1

                    # Part 2
                    while (a1[0] >= 0 and a1[0] < len(grid)) and (
                        a1[1] >= 0 and a1[1] < len(grid[0])
                    ):
                        if (
                            antinodesMap[a1[0]][a1[1]] == False
                            and grid[a1[0]][a1[1]] == "."
                        ):
                            print(key, a1)
                            antinodesMap[a1[0]][a1[1]] = True
                            antinodes += 1
                        a1 = (
                            round(a1[0] - dx * distance),
                            round(a1[1] - dy * distance),
                        )

                    while (a2[0] >= 0 and a2[0] < len(grid)) and (
                        a2[1] >= 0 and a2[1] < len(grid[0])
                    ):
                        if (
                            antinodesMap[a2[0]][a2[1]] == False
                            and grid[a2[0]][a2[1]] == "."
                        ):
                            print(key, a2)
                            antinodesMap[a2[0]][a2[1]] = True
                            antinodes += 1
                        a2 = (
                            round(a2[0] + dx * distance),
                            round(a2[1] + dy * distance),
                        )

    print("Number of unique antinodes's position: ", antinodes)


def main():
    parseInput()
    findNumberOfAntinodes()


if __name__ == "__main__":
    main()
