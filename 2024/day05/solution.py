instructions = {}
pagination = []
validPaginations = []
invalidPaginations = []


def parseInput():
    with open("input.txt") as file:
        for line in file:
            if "|" in line:
                n1, n2 = line.split("|")
                n1 = int(n1)
                n2 = int(n2)

                if n1 not in instructions:
                    instructions[n1] = [n2]
                else:
                    instructions[n1].append(n2)

            elif line == "" or line == "\n":
                continue
            else:
                lineArray = line.strip().split(",")
                temp = []
                for i in lineArray:
                    temp.append(int(i))
                pagination.append(temp)
                if isValidPagination(temp):
                    validPaginations.append(temp)
                else:
                    invalidPaginations.append(temp)


def isValidPagination(page) -> bool:
    for i in range(len(page) - 1):
        if page[i] not in instructions:
            return False
        else:
            pageWithoutI = page[i + 1 :]
            for j in range(len(pageWithoutI)):
                if pageWithoutI[j] not in instructions[page[i]]:
                    return False
    return True


def findMiddlePageNumbersSum():
    sum = 0
    for page in invalidPaginations:  # change to validPaginations for part 1
        sum += page[len(page) // 2]
    print("Sum: ", sum)


# Part 2


def orderIncorrectPages():
    for page in invalidPaginations:
        changed = True
        while changed:
            changed = False

            for i in range(len(page) - 1):
                currNumber = page[i]

                if currNumber not in instructions:
                    page.remove(currNumber)
                    page.append(currNumber)
                    changed = True
                    break

                for j in range(i + 1, len(page)):
                    nextNumber = page[j]

                    if nextNumber not in instructions[currNumber]:
                        page[i], page[j] = page[j], page[i]
                        changed = True
                        break

                if changed:
                    break


def main():
    parseInput()
    orderIncorrectPages()
    findMiddlePageNumbersSum()


if __name__ == "__main__":
    main()
