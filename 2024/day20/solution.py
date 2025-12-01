import networkx
from collections import deque

grid = []
movements = []
initial_position = (0, 0)
desination = (0, 0)
initial_path_lenght = 0


def parse_input():
    global grid
    global movements
    global initial_position
    global desination
    global initial_path_lenght
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(line.strip()))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "S":
                    initial_position = (i, j)
                elif grid[i][j] == "E":
                    desination = (i, j)
                else:
                    if grid[i][j] != "#":
                        initial_path_lenght += 1


def create_graph(labyrinth):
    G = networkx.Graph()
    rows, cols = len(labyrinth), len(labyrinth[0])

    for i in range(rows):
        for j in range(cols):
            if labyrinth[i][j] != "#":
                G.add_node((i, j))

    for i in range(rows):
        for j in range(cols):
            if labyrinth[i][j] != "#":
                for dx, dy in [(0, 1), (1, 0)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and labyrinth[nx][ny] != "#":
                        G.add_edge((i, j), (nx, ny))

    shortest_paths = dict(networkx.shortest_path_length(G, target=desination))

    return G, shortest_paths


def get_reachable(x, y, max_dist, rows, cols):
    reachable = []
    for dx in range(-max_dist, max_dist + 1):
        remaining_dist = max_dist - abs(dx)
        for dy in range(-remaining_dist, remaining_dist + 1):
            if dx == dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#":
                reachable.append((nx, ny))
    return reachable


def solve(G, shortest_paths, cheat_size):
    rows, cols = len(grid), len(grid[0])
    res = 0

    for node in G.nodes:
        i, j = node
        reachable = get_reachable(i, j, cheat_size, rows, cols)
        for nx, ny in reachable:
            cost = abs(i - nx) + abs(j - ny)
            savings = shortest_paths[(i, j)] - (shortest_paths[(nx, ny)] + cost)
            if savings >= 100:
                res += 1

    return res


def main():
    parse_input()
    G, shortest_paths = create_graph(grid)

    result1 = solve(G, shortest_paths, 2)
    result2 = solve(G, shortest_paths, 20)

    print(result1)
    print(result2)


if __name__ == "__main__":
    main()
