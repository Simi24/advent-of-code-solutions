import re

instructions = []


def parseInput():
    with open("input.txt") as file:
        for line in file:
            findSumOccurences(line)


def findSumOccurences(string):
    pattern = r"mul\(\d+,\d+\)"
    patternDo = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
    matches = re.findall(pattern, string)
    matchesDo = re.findall(patternDo, string)
    instructions.extend(matchesDo)


def multiplyNumbers(string) -> int:
    pattern = r"\d+"
    matches = re.findall(pattern, string)
    return int(matches[0]) * int(matches[1])


# Part 1
def findSum():
    sum = 0
    for instruction in instructions:
        sum += multiplyNumbers(instruction)

    print("Sum: ", sum)


# Part 2
def findValidSum():
    sum = 0
    isValid = True
    for instruction in instructions:
        print(instruction)
        if instruction == "don't()":
            isValid = False
            continue
        elif instruction == "do()":
            isValid = True
            continue

        if isValid:
            sum += multiplyNumbers(instruction)

    print("Sum: ", sum)


def main():
    parseInput()
    # findSum()
    findValidSum()


if __name__ == "__main__":
    main()
