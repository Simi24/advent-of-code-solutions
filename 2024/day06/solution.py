matrix = []
visited = []


def parseInput():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            matrix.append(row)


# Part 1
def findGuardPath():
    global visited
    position = (0, 0)
    direction = "^"
    visited = [[(False, "")] * len(matrix[0]) for _ in range(len(matrix))]

    numbersOfSteps = 0

    def findInitialPosition():
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == "^":
                    return (r, c)

    position = findInitialPosition()

    while True:
        if not visited[position[0]][position[1]][0]:
            visited[position[0]][position[1]] = (True, direction)
            numbersOfSteps += 1
        else:
            print("old direction: ", visited[position[0]][position[1]][1])
            print("new direction: ", direction)

        if direction == "^":
            if position[0] - 1 < 0:
                break
            if matrix[position[0] - 1][position[1]] == "#":
                direction = ">"
                position = (position[0], position[1] + 1)
            else:
                position = (position[0] - 1, position[1])
        elif direction == ">":
            if position[1] + 1 >= len(matrix[0]):
                break
            if matrix[position[0]][position[1] + 1] == "#":
                direction = "v"
                position = (position[0] + 1, position[1])
            else:
                position = (position[0], position[1] + 1)
        elif direction == "v":
            if position[0] + 1 >= len(matrix):
                break
            if matrix[position[0] + 1][position[1]] == "#":
                direction = "<"
                position = (position[0], position[1] - 1)
            else:
                position = (position[0] + 1, position[1])
        elif direction == "<":
            if position[1] - 1 < 0:
                break
            if matrix[position[0]][position[1] - 1] == "#":
                direction = "^"
                position = (position[0] - 1, position[1])
            else:
                position = (position[0], position[1] - 1)

    print(f"Number of steps: {numbersOfSteps}")


# Part 2
def guardPathHasCycle(modMatrix) -> bool:
    position = (0, 0)
    direction = "^"
    curPath = [[(False, "")] * len(modMatrix[0]) for _ in range(len(modMatrix))]

    numbersOfSteps = 0

    def findInitialPosition():
        for r in range(len(modMatrix)):
            for c in range(len(modMatrix[r])):
                if matrix[r][c] == "^":
                    return (r, c)

    position = findInitialPosition()

    while True:
        if not curPath[position[0]][position[1]][0]:
            curPath[position[0]][position[1]] = (True, direction)
            numbersOfSteps += 1
        elif curPath[position[0]][position[1]][1] == direction:
            return True

        if direction == "^":
            if position[0] - 1 < 0:
                break
            if modMatrix[position[0] - 1][position[1]] == "#":
                direction = ">"
                position = (position[0], position[1] + 1)
            else:
                position = (position[0] - 1, position[1])
        elif direction == ">":
            if position[1] + 1 >= len(modMatrix[0]):
                break
            if modMatrix[position[0]][position[1] + 1] == "#":
                direction = "v"
                position = (position[0] + 1, position[1])
            else:
                position = (position[0], position[1] + 1)
        elif direction == "v":
            if position[0] + 1 >= len(modMatrix):
                break
            if modMatrix[position[0] + 1][position[1]] == "#":
                direction = "<"
                position = (position[0], position[1] - 1)
            else:
                position = (position[0] + 1, position[1])
        elif direction == "<":
            if position[1] - 1 < 0:
                break
            if modMatrix[position[0]][position[1] - 1] == "#":
                direction = "^"
                position = (position[0] - 1, position[1])
            else:
                position = (position[0], position[1] - 1)

    print(f"Number of steps: {numbersOfSteps}")
    return False


def numberObstructionPosition():
    n = 0
    for p in range(len(visited)):
        for q in range(len(visited[p])):
            if visited[p][q][0] and matrix[p][q] != "^":
                matrixCopy = matrix.copy()
                matrixCopy[p][q] = "#"
                print("added obstruction at position: ", p, q)

                if guardPathHasCycle(matrixCopy):
                    n += 1

                matrixCopy[p][q] = "."

    print("Number of paths with cycle: ", n)


def main():
    parseInput()
    findGuardPath()
    numberObstructionPosition()


if __name__ == "__main__":
    main()
