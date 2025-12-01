from typing import List

calibrations = {}


def parseInput():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip().split(":"))
            row[1] = row[1].strip()
            calibrations[int(row[0])] = [int(x) for x in row[1].strip().split(" ")]


def findCombinationEquation(nums: List[int], target: int) -> int:
    setCorrectResult = set()
    correct_results = []
    res = 0
    partial = 0

    # Part 1
    def dfs(i):
        nonlocal partial
        if partial == target:
            nonlocal res
            if target not in setCorrectResult:
                setCorrectResult.add(target)
                res += target
            return
        if partial > target:
            return
        if i == len(nums):
            return

        # choose to sum
        partial += nums[i]
        dfs(i + 1)
        partial -= nums[i]

        # choose to multiply
        original_partial = partial
        partial *= nums[i]
        dfs(i + 1)
        partial = original_partial

        # choose to merge
        original_partial = partial
        partial = partial * 10 ** (len(str(nums[i]))) + nums[i]
        dfs(i + 1)
        partial = original_partial

    # Part 2 -> changed to dfs2 to avoid problem with division precision
    def dfs2(index: int, current_value: int):
        if index == len(nums):
            if current_value == target and target not in correct_results:
                correct_results.append(target)
            return

        # choose to sum
        dfs2(index + 1, current_value + nums[index])

        # choose to multiply
        dfs2(index + 1, current_value * nums[index])

        # choose to merge
        dfs2(index + 1, int(str(current_value) + str(nums[index])))

    # dfs(0)
    dfs2(0, 0)
    res += sum(correct_results)
    return res


def findCombinationEquations() -> int:
    res = 0
    for key in calibrations:
        res += findCombinationEquation(calibrations[key], key)
    return res


def main():
    parseInput()
    print(findCombinationEquations())


if __name__ == "__main__":
    main()
