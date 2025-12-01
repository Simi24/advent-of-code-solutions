matrix = []
rows = 0
cols = 0


def parseInput():
    global matrix, rows, cols
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            matrix.append([int(x) for x in row])
    rows = len(matrix)
    cols = len(matrix[0])


# Find the neighbors of a node (vertial and horizontal)
def get_neighbors(node):
    global matrix, rows, cols
    i, j = node
    neighbors = []
    if i > 0:  # up
        neighbors.append((i - 1, j))
    if i < rows - 1:  # down
        neighbors.append((i + 1, j))
    if j > 0:  # left
        neighbors.append((i, j - 1))
    if j < cols - 1:  # right
        neighbors.append((i, j + 1))

    return neighbors


def find_paths(start_node, current_value):
    global matrix, rows, cols
    stack = [(start_node, current_value)]
    paths_to_9 = 0
    unique_paths_to_9 = 0
    visited9 = set()

    while stack:
        node, value = stack.pop()
        for neighbor in get_neighbors(node):
            ni, nj = neighbor
            if matrix[ni][nj] == value + 1:
                if matrix[ni][nj] == 9:
                    if neighbor not in visited9:
                        unique_paths_to_9 += 1
                        visited9.add(neighbor)
                    paths_to_9 += 1
                else:
                    stack.append((neighbor, matrix[ni][nj]))

    return paths_to_9, unique_paths_to_9


def findValidPaths():
    global matrix, rows, cols
    start_nodes = [
        (i, j) for i in range(rows) for j in range(cols) if matrix[i][j] == 0
    ]

    total_paths = 0
    total_unique_paths = 0

    for start in start_nodes:
        paths, unique_paths = find_paths(start, 0)
        total_paths += paths
        total_unique_paths += unique_paths

    # Part 1
    print("Total unique paths to 9: ", total_unique_paths)
    # Part 2
    print("Total paths to 9: ", total_paths)

    return total_paths


def main():
    parseInput()
    findValidPaths()


if __name__ == "__main__":
    main()
