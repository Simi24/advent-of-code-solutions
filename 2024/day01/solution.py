list_location1 = []
list_location2 = []


def parseInput():
    with open("input.txt") as file:
        for line in file:
            array = line.split()
            list_location1.append(array[0])
            list_location2.append(array[1])


def findLocation():
    parseInput()
    totalDistance = 0
    list_location1.sort()
    list_location2.sort()

    for i in range(len(list_location1)):
        totalDistance += abs(int(list_location1[i]) - int(list_location2[i]))

    print("Total distance: ", totalDistance)


def findLocationSimilarityScore():
    totalDistance = 0
    list_location2_occurrences = {}
    for n in list_location2:
        if n in list_location2_occurrences:
            list_location2_occurrences[n] += 1
        else:
            list_location2_occurrences[n] = 1

    for i in range(len(list_location1)):
        if list_location1[i] in list_location2_occurrences:
            totalDistance += (
                int(list_location1[i]) * list_location2_occurrences[list_location1[i]]
            )

    print("Total distance similarity score: ", totalDistance)


def main():
    findLocation()
    findLocationSimilarityScore()


if __name__ == "__main__":
    main()
