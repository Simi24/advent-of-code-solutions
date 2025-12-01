from collections import defaultdict


class BinaryAdder:
    def __init__(self):
        self.forward_gates = {}
        self.reverse_gates = {}
        self.output_wires = set()

    def parse_input(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            reading_wires = True

            for line in lines:
                line = line.strip()
                if not line:
                    reading_wires = False
                    continue

                if reading_wires:
                    continue
                else:
                    if "->" in line:
                        left, output = line.split("->")
                        parts = left.strip().split()
                        input1, op, input2 = parts
                        output = output.strip()

                        if input1 > input2:
                            input1, input2 = input2, input1

                        self.forward_gates[(input1, input2, op)] = output
                        self.reverse_gates[output] = (input1, input2, op)

    def swap_wires(self, wire1, wire2):
        """Scambia gli output di due gate"""
        gate1 = self.reverse_gates[wire1]
        gate2 = self.reverse_gates[wire2]

        self.forward_gates[gate1], self.forward_gates[gate2] = self.forward_gates[gate2], self.forward_gates[gate1]
        self.reverse_gates[wire1], self.reverse_gates[wire2] = self.reverse_gates[wire2], self.reverse_gates[wire1]

    def find_swapped_wires(self):
        max_bit = 0
        for wire in self.reverse_gates:
            if wire.startswith("z") and wire[1:].isdigit():
                max_bit = max(max_bit, int(wire[1:]))

        carry = ""
        for i in range(max_bit):
            x = f"x{i:02}"
            y = f"y{i:02}"
            z = f"z{i:02}"

            xor_out = self.forward_gates.get((x, y, "XOR"))
            and_out = self.forward_gates.get((x, y, "AND"))

            if not carry:
                carry = and_out
            else:
                a, b = (carry, xor_out) if carry <= xor_out else (xor_out, carry)
                key = (a, b, "XOR")

                if key not in self.forward_gates:
                    gate_inputs = set(self.reverse_gates[z][:2])
                    key_inputs = {a, b}
                    swapped_wires = list(gate_inputs ^ key_inputs)
                    self.output_wires.add(swapped_wires[0])
                    self.output_wires.add(swapped_wires[1])
                    self.swap_wires(swapped_wires[0], swapped_wires[1])
                elif self.forward_gates[key] != z:
                    current_output = self.forward_gates[key]
                    self.output_wires.add(current_output)
                    self.output_wires.add(z)
                    self.swap_wires(z, current_output)

                xor_out = self.forward_gates.get((x, y, "XOR"))
                and_out = self.forward_gates.get((x, y, "AND"))

                a, b = (carry, xor_out) if carry <= xor_out else (xor_out, carry)
                carry = self.forward_gates.get((a, b, "AND"))
                a, b = (carry, and_out) if carry <= and_out else (and_out, carry)
                carry = self.forward_gates.get((a, b, "OR"))

        return sorted(self.output_wires)


def main():
    adder = BinaryAdder()
    adder.parse_input("input.txt")

    swapped_wires = adder.find_swapped_wires()
    if swapped_wires:
        print(",".join(swapped_wires))
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
