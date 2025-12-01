class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def move_grid(self, grid):
        self.p = (self.p[0] + self.v[0], self.p[1] + self.v[1])
        if self.p[0] < 0:
            self.p = (len(grid[0]) - 1, self.p[1])
        elif self.p[0] >= len(grid[0]):
            self.p = (0, self.p[1])
        if self.p[1] < 0:
            self.p = (self.p[0], len(grid) - 1)
        elif self.p[1] >= len(grid):
            self.p = (self.p[0], 0)

        return grid[self.p[1]][self.p[0]]

    def move(self, row_len, columns):
        if self.p[0] + self.v[0] < 0:
            self.p = (row_len - abs(self.p[0] + self.v[0]), self.p[1])
        elif self.p[0] + self.v[0] >= row_len:
            self.p = (self.p[0] + self.v[0] - row_len, self.p[1])
        else:
            self.p = (self.p[0] + self.v[0], self.p[1])
        if self.p[1] + self.v[1] < 0:
            self.p = (self.p[0], columns - abs(self.p[1] + self.v[1]))
        elif self.p[1] + self.v[1] >= columns:
            self.p = (self.p[0], self.p[1] + self.v[1] - columns)
        else:
            self.p = (self.p[0], self.p[1] + self.v[1])

        return self.p

    def print(self):
        print(f"Position: {self.p}, Velocity: {self.v}")


robots = []


def parse_input():
    with open("input.txt") as file:
        global robots
        lines = file.readlines()
        for line in lines:
            _p = line.strip().split(" ")[0]
            _v = line.strip().split(" ")[1]
            px = int(_p.split("=")[1].split(",")[0])
            py = int(_p.split("=")[1].split(",")[1])
            p = (px, py)
            vx = int(_v.split("=")[1].split(",")[0])
            vy = int(_v.split("=")[1].split(",")[1])
            v = (vx, vy)
            robot = Robot(p, v)
            robots.append(robot)


def find_final_position():
    global robots

    row_len = 101
    columns = 103
    # for robot in robots:
    #     for i in range(0, 100):
    #         robot.move(row_len, columns)
    # draw_matrix_with_robots(row_len, columns)
    i = 0
    while True:
        i += 1
        positions = set()
        for robot in robots:
            robot.move(row_len, columns)

        for robot in robots:
            if robot.p in positions:
                break
            else:
                positions.add(robot.p)

        if len(positions) == len(robots):
            print(f"Seconds: {i + 1}")
            draw_matrix_with_robots(row_len, columns)
            break

        positions.clear()


def draw_matrix_with_robots(row_len, columns):
    global robots
    matrix = [["." for i in range(row_len)] for j in range(columns)]
    for robot in robots:
        if matrix[robot.p[1]][robot.p[0]] != ".":
            matrix[robot.p[1]][robot.p[0]] = int(matrix[robot.p[1]][robot.p[0]]) + 1
        else:
            matrix[robot.p[1]][robot.p[0]] = 1
    print("\n".join(" ".join(f"{cell:>2}" for cell in row) for row in matrix))

    def find_robots_in_quadrants():
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == ".":
                    continue
                if r < len(matrix) // 2 and c < len(matrix[0]) // 2:
                    q1 += matrix[r][c]
                elif r < len(matrix) // 2 and c > len(matrix[0]) // 2:
                    q2 += matrix[r][c]
                elif r > len(matrix) // 2 and c < len(matrix[0]) // 2:
                    q3 += matrix[r][c]
                elif r > len(matrix) // 2 and c > len(matrix[0]) // 2:
                    q4 += matrix[r][c]

        print(f"Q1 * Q2 * Q3 * Q4: {q1 * q2 * q3 * q4}")

    find_robots_in_quadrants()


def main():
    parse_input()
    find_final_position()


if __name__ == "__main__":
    main()
