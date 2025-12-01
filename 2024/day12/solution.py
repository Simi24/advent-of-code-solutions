from collections import defaultdict


matrix = []
rows = 0
cols = 0


def parseInput():
    global matrix, rows, cols
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            matrix.append(row)
    rows = len(matrix)
    cols = len(matrix[0])


def findTotalPriceFences():
    global matrix, rows, cols

    def dfs(i, j, visited, target, edges):
        if (
            i < 0
            or i >= rows
            or j < 0
            or j >= cols
            or matrix[i][j] != target
            or (i, j) in visited
        ):
            return 0, 0

        visited.add((i, j))
        area = 1
        perimeter = 4

        # Check outer edges, there is a outer edge if the neighbors in each pair of orthogonal directions are different from the target
        if (i - 1 < 0 or matrix[i - 1][j] != target) and (
            j + 1 >= cols or matrix[i][j + 1] != target
        ):
            edges[(i, j)] += 1
        if (i - 1 < 0 or matrix[i - 1][j] != target) and (
            j - 1 < 0 or matrix[i][j - 1] != target
        ):
            edges[(i, j)] += 1
        if (i + 1 >= rows or matrix[i + 1][j] != target) and (
            j + 1 >= cols or matrix[i][j + 1] != target
        ):
            edges[(i, j)] += 1
        if (i + 1 >= rows or matrix[i + 1][j] != target) and (
            j - 1 < 0 or matrix[i][j - 1] != target
        ):
            edges[(i, j)] += 1

        # Check inner edges, there is a inner edge if the neighbors in each pair of orthogonal directions are equal to the target and the diagonal neighbor is different from the target
        if (
            (i - 1 >= 0 and matrix[i - 1][j] == target)
            and (j + 1 < cols and matrix[i][j + 1] == target)
            and (i - 1 >= 0 and j + 1 < cols and matrix[i - 1][j + 1] != target)
        ):
            edges[(i, j)] += 1
        if (
            (i - 1 >= 0 and matrix[i - 1][j] == target)
            and (j - 1 >= 0 and matrix[i][j - 1] == target)
            and (i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] != target)
        ):
            edges[(i, j)] += 1
        if (
            (i + 1 < rows and matrix[i + 1][j] == target)
            and (j + 1 < cols and matrix[i][j + 1] == target)
            and (i + 1 < rows and j + 1 < cols and matrix[i + 1][j + 1] != target)
        ):
            edges[(i, j)] += 1
        if (
            (i + 1 < rows and matrix[i + 1][j] == target)
            and (j - 1 >= 0 and matrix[i][j - 1] == target)
            and (i + 1 < rows and j - 1 >= 0 and matrix[i + 1][j - 1] != target)
        ):
            edges[(i, j)] += 1

        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == target:
                perimeter -= 1

        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            sub_area, sub_perimeter = dfs(ni, nj, visited, target, edges)
            area += sub_area
            perimeter += sub_perimeter

        return area, perimeter

    visited = set()
    fencesCost = 0
    discount_fence_cost = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                edges = defaultdict(int)
                area, perimeter = dfs(i, j, visited, matrix[i][j], edges)
                fencesCost += area * perimeter
                discount_fence_cost += area * sum(edges.values())

    print("Fences cost: ", fencesCost)
    print("Discounted fence cost: ", discount_fence_cost)
    return fencesCost


def main():
    parseInput()
    findTotalPriceFences()


if __name__ == "__main__":
    main()
