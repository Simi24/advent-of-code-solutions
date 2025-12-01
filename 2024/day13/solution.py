# A -> 3 B -> 1
class Claw_Machine:
    def __init__(self, A, B, prize):
        self.A = A
        self.B = B
        self.prize = prize

    def print(self):
        print(f"A: {self.A}, B: {self.B}, Prize: {self.prize}")


claw_machines = []


def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()
        claw_machine = Claw_Machine(None, None, None)
        for line in lines:
            if line.strip() == "":
                claw_machines.append(claw_machine)
                claw_machine = Claw_Machine(None, None, None)
            else:
                if line.__contains__("A"):
                    _A = line.strip().split(":")[1]
                    x = int(_A.split(",")[0].split("+")[1])
                    y = int(_A.split(",")[1].split("+")[1])
                    A = (x, y)
                    claw_machine.A = A
                elif line.__contains__("B"):
                    _B = line.strip().split(":")[1]
                    x = int(_B.split(",")[0].split("+")[1])
                    y = int(_B.split(",")[1].split("+")[1])
                    B = (x, y)
                    claw_machine.B = B
                elif line.__contains__("Prize"):
                    prize = line.strip().split(":")[1]
                    x = int(prize.split(",")[0].split("=")[1])
                    y = int(prize.split(",")[1].split("=")[1])
                    prize = (x, y)
                    claw_machine.prize = prize

            if lines.index(line) == len(lines) - 1:
                claw_machines.append(claw_machine)


# Solving linear system of equation using Cramer's rule
def solve_linear_system(A, B, prize):
    x_A, y_A = A
    x_B, y_B = B
    x_prize, y_prize = prize

    det = x_A * y_B - x_B * y_A
    det_x = x_prize * y_B - x_B * y_prize
    det_y = x_A * y_prize - x_prize * y_A

    a_candidates = []
    b_candidates = []

    for a in range(max(0, det_x // det - 10), det_x // det + 10):
        for b in range(max(0, det_y // det - 10), det_y // det + 10):
            if x_A * a + x_B * b == x_prize and y_A * a + y_B * b == y_prize:
                a_candidates.append(a)
                b_candidates.append(b)

    min_tokens = float("inf")
    best_a, best_b = 0, 0

    for a, b in zip(a_candidates, b_candidates):
        tokens = 3 * a + b
        if tokens < min_tokens:
            min_tokens = tokens
            best_a, best_b = a, b

    return best_a, best_b


def findFewestTokens(claw_machine):
    A = (claw_machine.A[0], claw_machine.A[1])
    B = (claw_machine.B[0], claw_machine.B[1])
    prize = (claw_machine.prize[0], claw_machine.prize[1])
    price = 0
    a, b = solve_linear_system(A, B, prize)
    print(a, b)
    # if (a < 100 and b < 100): price = a * 3 + b
    price = a * 3 + b
    return price


def main():
    parse_input()

    tot = 0
    for claw_machine in claw_machines:
        claw_machine.print()
        claw_machine.prize = (
            claw_machine.prize[0] + 10000000000000,
            claw_machine.prize[1] + 10000000000000,
        )
        price = findFewestTokens(claw_machine)
        print(price)
        tot += price

    print("TOT: ", tot)


if __name__ == "__main__":
    main()
