matrix = []


def parseInput():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            matrix.append(row)


# Part 1
def findXmasOccurrences():
    numXmas = 0
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "X" and not visited[r][c]:

                def mark_and_count(start_r, start_c, dr, dc):
                    nonlocal numXmas
                    if 0 <= start_r + 3 * dr < len(
                        matrix
                    ) and 0 <= start_c + 3 * dc < len(matrix[0]):
                        if (
                            matrix[start_r + dr][start_c + dc] == "M"
                            and matrix[start_r + 2 * dr][start_c + 2 * dc] == "A"
                            and matrix[start_r + 3 * dr][start_c + 3 * dc] == "S"
                        ):
                            visited[start_r][start_c] = True
                            visited[start_r + dr][start_c + dc] = True
                            visited[start_r + 2 * dr][start_c + 2 * dc] = True
                            visited[start_r + 3 * dr][start_c + 3 * dc] = True

                            print(f"XMAS found at row {start_r}, column {start_c}")
                            numXmas += 1
                            return True
                    return False

                mark_and_count(r, c, 0, 1)
                mark_and_count(r, c, 0, -1)
                mark_and_count(r, c, 1, 0)
                mark_and_count(r, c, -1, 0)
                mark_and_count(r, c, 1, 1)
                mark_and_count(r, c, -1, -1)
                mark_and_count(r, c, 1, -1)
                mark_and_count(r, c, -1, 1)

    print(f"Number of XMAS occurrences: {numXmas}")


# Part 2
def findX_MasOccurrences():
    numX_Mas = 0
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "A" and not visited[r][c]:
                if (
                    r + 1 < len(matrix)
                    and c + 1 < len(matrix[0])
                    and r - 1 >= 0
                    and c - 1 >= 0
                ):
                    if (
                        (matrix[r - 1][c + 1] == "M" and matrix[r + 1][c - 1] == "S")
                        or (matrix[r - 1][c + 1] == "S" and matrix[r + 1][c - 1] == "M")
                    ) and (
                        (matrix[r - 1][c - 1] == "M" and matrix[r + 1][c + 1] == "S")
                        or (matrix[r - 1][c - 1] == "S" and matrix[r + 1][c + 1] == "M")
                    ):
                        visited[r][c] = True
                        numX_Mas += 1
                        print(
                            matrix[r - 1][c + 1],
                            matrix[r + 1][c - 1],
                            matrix[r - 1][c - 1],
                            matrix[r + 1][c + 1],
                        )
                        print(f"X_Mas found at row {r}, column {c}")

    print(f"Number of X_Mas occurrences: {numX_Mas}")


def main():
    parseInput()
    findXmasOccurrences()
    findX_MasOccurrences()


if __name__ == "__main__":
    main()
