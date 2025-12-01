from collections import deque

_bytes = []


def parse_input():
    global _bytes
    with open("input.txt") as file:
        for line in file:
            l = line.strip().split(",")
            _bytes.append((int(l[1]), int(l[0])))


def create_matrix():
    matrix = [["." for x in range(71)] for y in range(71)]
    for i in range(1024):
        matrix[_bytes[i][0]][_bytes[i][1]] = "#"

    return matrix


def find_shortest_path_bfs(labyrinth, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(labyrinth), len(labyrinth[0])

    pq = deque([(0, start[0], start[1])])
    visited = set()

    while pq:
        current_dist, x, y = pq.popleft()
        if (x, y) == end:
            return current_dist

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and labyrinth[nx][ny] != "#":
                total_dist = current_dist + 1
                pq.append((total_dist, nx, ny))

    return -1


def find_first_blocking_block(matrix):
    for i in range(1024, 3451):
        matrix[_bytes[i][0]][_bytes[i][1]] = "#"
        if find_shortest_path_bfs(matrix, (0, 0), (70, 70)) == -1:
            return (_bytes[i][1], _bytes[i][0])


def main():
    parse_input()
    matrix = create_matrix()

    print("Shortest path: ", find_shortest_path_bfs(matrix, (0, 0), (70, 70)))
    print("First blocking block: ", find_first_blocking_block(matrix))


if __name__ == "__main__":
    main()
