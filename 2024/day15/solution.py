from enum import Enum


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def delta(self):
        return self.value


class Robot:
    grid = []
    SYMBOL_TO_DIRECTION = {
        "^": Direction.UP,
        "v": Direction.DOWN,
        "<": Direction.LEFT,
        ">": Direction.RIGHT,
    }

    def __init__(self, position):
        self.position = position

    def set_grid(self, grid):
        self.grid = grid

    def print_grid(self):
        print("\n".join("".join(row) for row in self.grid))
        print("-" * 20)

    # Part 1
    def move(self, direction):
        new_position = (
            self.position[0] + direction.delta[0],
            self.position[1] + direction.delta[1],
        )
        if self.grid[new_position[1]][new_position[0]] == "#":
            return False
        elif self.grid[new_position[1]][new_position[0]] == "O":
            new_position_O = new_position
            O_positions = []
            while self.grid[new_position_O[1]][new_position_O[0]] == "O":
                new_position_O = (
                    new_position_O[0] + direction.delta[0],
                    new_position_O[1] + direction.delta[1],
                )
                if self.grid[new_position_O[1]][new_position_O[0]] == "O":
                    O_positions.append(new_position_O)
                elif self.grid[new_position_O[1]][new_position_O[0]] == "#":
                    return False
                elif self.grid[new_position_O[1]][new_position_O[0]] == ".":
                    O_positions.append(new_position_O)
                    grid[self.position[1]][self.position[0]] = "."
                    self.position = new_position
                    grid[new_position[1]][new_position[0]] = "@"
                    for pos in O_positions:
                        grid[pos[1]][pos[0]] = "O"
                    return True
        else:
            grid[self.position[1]][self.position[0]] = "."
            self.position = new_position
            grid[new_position[1]][new_position[0]] = "@"
            return True

    # Part 2
    def move_with_modified_grid(self, direction):
        new_position = (
            self.position[0] + direction.delta[0],
            self.position[1] + direction.delta[1],
        )
        if self.grid[new_position[1]][new_position[0]] == "#":
            return False
        elif (
            self.grid[new_position[1]][new_position[0]] == "["
            or self.grid[new_position[1]][new_position[0]] == "]"
        ):
            if direction == Direction.LEFT or direction == Direction.RIGHT:
                final_position = new_position
                while True:
                    final_position = (
                        final_position[0] + direction.delta[0],
                        final_position[1] + direction.delta[1],
                    )
                    if self.grid[final_position[1]][final_position[0]] == ".":
                        self.grid[final_position[1]].pop(final_position[0])
                        self.grid[self.position[1]].insert(self.position[0], ".")
                        self.position = new_position
                        return True
                    elif self.grid[final_position[1]][final_position[0]] == "#":
                        return False

            # UP/DOWN
            else:
                layer = {}
                layer[new_position] = set([self.position])
                moves = []
                visited = set()

                while layer:
                    new_layer = {}
                    for crate_pos in layer:
                        if self.grid[crate_pos[1]][crate_pos[0]] not in ["[", "]"]:
                            continue

                        if self.grid[crate_pos[1]][crate_pos[0]] == "[":
                            left_pos = crate_pos
                            right_pos = (crate_pos[0] + 1, crate_pos[1])
                        elif self.grid[crate_pos[1]][crate_pos[0]] == "]":
                            left_pos = (crate_pos[0] - 1, crate_pos[1])
                            right_pos = crate_pos
                        if (left_pos, right_pos) in visited:
                            continue

                        visited.add((left_pos, right_pos))
                        new_left_pos = (
                            left_pos[0] + direction.delta[0],
                            left_pos[1] + direction.delta[1],
                        )
                        new_right_pos = (
                            right_pos[0] + direction.delta[0],
                            right_pos[1] + direction.delta[1],
                        )

                        if (
                            self.grid[new_left_pos[1]][new_left_pos[0]] == "#"
                            or self.grid[new_right_pos[1]][new_right_pos[0]] == "#"
                        ):
                            return False

                        for prev_pos in layer[crate_pos]:
                            moves.append((left_pos, new_left_pos))
                            moves.append((right_pos, new_right_pos))

                        new_layer[new_left_pos] = set([left_pos])
                        new_layer[new_right_pos] = set([right_pos])

                    layer = new_layer

                # Movements in reverse order
                while moves:
                    old, new = moves.pop()

                    if self.grid[old[1]][old[0]] not in ["[", "]"]:
                        raise ValueError(f"Error: invalid old value: {old}")
                    if self.grid[new[1]][new[0]] != ".":
                        raise ValueError(
                            f"Error: Position {new} already occupied by {self.grid[new[1]][new[0]]}"
                        )

                    # Move one crate
                    crate_char = self.grid[old[1]][old[0]]
                    self.grid[old[1]][old[0]] = "."
                    self.grid[new[1]][new[0]] = crate_char

                new_robot_pos = (
                    self.position[0] + direction.delta[0],
                    self.position[1] + direction.delta[1],
                )

                if self.grid[new_robot_pos[1]][new_robot_pos[0]] not in [".", "[", "]"]:
                    raise ValueError(f"Error: Robot cannot move in {new_robot_pos}")

                self.grid[self.position[1]][self.position[0]] = "."
                self.grid[new_robot_pos[1]][new_robot_pos[0]] = "@"
                self.position = new_robot_pos

        else:
            self.grid[self.position[1]][self.position[0]] = "."
            self.position = new_position
            self.grid[new_position[1]][new_position[0]] = "@"
            return True


grid = []
movements = []
initial_position = (0, 0)
robot = Robot(initial_position)


def parse_input():
    global grid
    global movements
    global initial_position
    global robot
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.__contains__("#"):
                grid.append(list(line.strip()))
            elif line == "":
                continue
            else:
                movements.extend(line.strip())

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@":
                    initial_position = (j, i)
                    break

        robot = Robot(initial_position)
        robot.set_grid(grid)


def robot_track():
    global robot
    global movements
    print("Initial state:")
    robot.print_grid()
    for movement in movements:
        direction = Robot.SYMBOL_TO_DIRECTION[movement]
        print(f"Moving to: {movement}")
        robot.move(direction)
        robot.print_grid()
        print()

    grid = robot.grid
    sum_GPS = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                GPS = (100 * (i)) + (j)
                sum_GPS += GPS

    print(f"Sum of GPS: {sum_GPS}")


def modify_grid():
    global robot
    global grid
    robot.set_grid(grid)

    new_grid = []

    for r in range(len(grid)):
        new_grid.append([])
        for c in range(len(grid[r])):
            if grid[r][c] == "#":
                new_grid[r].append("#")
                new_grid[r].append("#")
            elif grid[r][c] == ".":
                new_grid[r].append(".")
                new_grid[r].append(".")
            elif grid[r][c] == "@":
                new_grid[r].append("@")
                new_grid[r].append(".")
            elif grid[r][c] == "O":
                new_grid[r].append("[")
                new_grid[r].append("]")

    for r in range(len(new_grid)):
        for c in range(len(new_grid[r])):
            if new_grid[r][c] == "@":
                robot.position = (c, r)
                break

    robot.set_grid(new_grid)


def robot_track_with_modified_grid():
    global robot
    global movements
    print("Initial state:")
    robot.print_grid()
    for movement in movements:
        direction = Robot.SYMBOL_TO_DIRECTION[movement]
        print(f"Moving to: {movement}")
        robot.move_with_modified_grid(direction)
        robot.print_grid()
        print()

    grid = robot.grid
    sum_GPS = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                GPS = (100 * (i)) + (j)
                sum_GPS += GPS

    print(f"Sum of GPS: {sum_GPS}")


def main():
    parse_input()
    # robot_track()
    modify_grid()
    robot_track_with_modified_grid()


if __name__ == "__main__":
    main()
