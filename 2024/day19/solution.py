patterns = []
towels = []


def parse_input():
    global patterns
    with open("input.txt") as file:
        for line in file:
            if line.__contains__(","):
                patterns = [x.strip() for x in line.strip().split(",")]
            elif line == "\n":
                continue
            else:
                towels.append(line.strip())


def can_towel_be_created_from_patterns(towel, patterns):
    memo = {}

    def dfs(index):
        if index in memo:
            return memo[index]

        if index == len(towel):
            return True

        for pattern in patterns:
            if towel[index:].startswith(pattern):
                if dfs(index + len(pattern)):
                    memo[index] = True
                    return True

        memo[index] = False
        return False

    return dfs(0)


def find_all_possible_combinations(towel, patterns):
    memo = {}

    def dfs(index):
        if index in memo:
            return memo[index]

        if index == len(towel):
            return 1

        total = 0
        for pattern in patterns:
            if towel[index:].startswith(pattern):
                total += dfs(index + len(pattern))

        memo[index] = total
        return total

    return dfs(0)


def main():
    parse_input()

    valid_towels = 0
    total_combinations = 0

    for towel in towels:
        if can_towel_be_created_from_patterns(towel, patterns):
            valid_towels += 1

    for towel in towels:
        total_combinations += find_all_possible_combinations(towel, patterns)

    print("Valid towels: ", valid_towels)
    print("Total valid combinations: ", total_combinations)


if __name__ == "__main__":
    main()
