import math


class Computer:

    output = ""
    instruction_pointer = 0

    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.program = program

    def run(self):
        self.output = ""
        self.instruction_pointer = 0
        while self.instruction_pointer < len(self.program) - 1:
            self.execute_instruction()
        return self.output

    # Utility functions

    def print_output(self):
        print(self.output)

    def print_registers(self):
        print(f"A: {self.A}, B: {self.B}, C: {self.C}")

    def get_value_combo_operand(self, operand):
        if operand >= 0 and operand <= 3:
            return operand
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C

    def get_operand(self):
        return self.program[self.instruction_pointer + 1]

    def execute_instruction(self):
        if self.program[self.instruction_pointer] == 0:
            return self.adv()
        elif self.program[self.instruction_pointer] == 1:
            return self.bxl()
        elif self.program[self.instruction_pointer] == 2:
            return self.bst()
        elif self.program[self.instruction_pointer] == 3:
            return self.jnz()
        elif self.program[self.instruction_pointer] == 4:
            return self.bxc()
        elif self.program[self.instruction_pointer] == 5:
            return self.out()
        elif self.program[self.instruction_pointer] == 6:
            return self.bdv()
        elif self.program[self.instruction_pointer] == 7:
            return self.cdv()

    def set_registers(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def set_program(self, program):
        self.program = program

    # Instructions

    def adv(self):
        self.A = int(
            self.A // math.pow(2, self.get_value_combo_operand(self.get_operand()))
        )
        self.instruction_pointer += 2

    def bxl(self):
        # Bitwise XOR
        self.B = self.B ^ self.get_operand()
        self.instruction_pointer += 2

    def bst(self):
        self.B = self.get_value_combo_operand(self.get_operand()) % 8
        self.instruction_pointer += 2

    def jnz(self):
        if self.A != 0:
            self.instruction_pointer = self.get_operand()
        else:
            self.instruction_pointer += 2

    def bxc(self):
        operand = self.get_operand()
        self.B = self.B ^ self.C
        self.instruction_pointer += 2

    def out(self):
        if len(self.output) > 0:
            self.output += ","
        self.output += str(self.get_value_combo_operand(self.get_operand()) % 8)
        self.instruction_pointer += 2

    def bdv(self):
        self.B = int(
            self.A // math.pow(2, self.get_value_combo_operand(self.get_operand()))
        )
        self.instruction_pointer += 22

    def cdv(self):
        self.C = int(
            self.A // math.pow(2, self.get_value_combo_operand(self.get_operand()))
        )
        self.instruction_pointer += 2


registers = []
program = []
computer = Computer(0, 0, 0, program)


def parse_input():
    global registers
    global program
    global computer
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.__contains__("Program"):
                pg = list(line.strip().split(":")[1].strip().split(","))
                program = [int(x) for x in pg]
            elif line != "\n":
                reg = int(line.split(":")[1].strip())
                registers.append(reg)

    computer.set_registers(registers[0], registers[1], registers[2])
    computer.set_program(program)


import heapq


def main():
    global computer
    parse_input()

    # Part 1
    print(computer.run())

    # Part 2
    variants = []
    heapq.heappush(variants, (len(program) - 1, 0))

    while variants:
        offset, a = heapq.heappop(variants)

        for i in range(8):
            next_a = (a << 3) + i  # shift left by 3 bits -> multiply by 8
            computer.set_registers(next_a, 0, 0)
            output = computer.run().split(",")
            expected_output = [str(x) for x in program[offset:]]

            if output == expected_output:
                if offset == 0:
                    print(f"A: {next_a}")
                    return
                heapq.heappush(variants, (offset - 1, next_a))

    print("No A found")


if __name__ == "__main__":
    main()
