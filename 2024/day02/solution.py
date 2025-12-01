reports = []


def parseInput():
    with open("input.txt") as file:
        for line in file:
            array = line.split()
            temp = []
            for i in range(len(array)):
                temp.append(int(array[i]))

            reports.append(temp)


# PART 1
def isIncreasing(array):
    for i in range(len(array)):
        if i == 0:
            continue
        if array[i] <= array[i - 1]:
            return False
    return True


def isDecreasing(array):
    for i in range(len(array)):
        if i == 0:
            continue
        if array[i] >= array[i - 1]:
            return False
    return True


def isValidReport(report):
    if isDecreasing(report) or isIncreasing(report):
        for i in range(len(report)):
            if i == 0:
                continue
            if abs(report[i] - report[i - 1]) > 3:
                return False
        return True


# PART 2
def isValidReportRemovingElement(report):
    temp = report
    for i in range(len(report)):
        temp = report[:i] + report[i + 1 :]
        if isValidReport(temp):
            return True
    return False


def main():
    parseInput()
    validReports = 0
    for report in reports:
        if isValidReport(report):
            validReports += 1
        else:
            if isValidReportRemovingElement(report):
                validReports += 1
    print("Valid reports: ", validReports)


if __name__ == "__main__":
    main()
