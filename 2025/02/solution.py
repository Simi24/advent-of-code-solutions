from collections import defaultdict


ids = []
all_ids_ranges = []


def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
        for line in lines:
            ids.extend(line.strip().split(","))

        for _range in ids:
            bounds = _range.split("-")
            for id in range(int(bounds[0]), int(bounds[1]) + 1):
                all_ids_ranges.append(str(id))


def is_valid_id_part1(id: int) -> bool:
    return id[: len(id) // 2] != id[len(id) // 2 :]


def solve_part1(ids: list[str]) -> int:
    sum_invalid_ids = 0
    checked_ids = defaultdict(bool)
    for id in ids:
        if len(id) % 2 != 0:
            continue
        if id in checked_ids:
            if not checked_ids[id]:
                sum_invalid_ids += int(id)
            continue
        if not is_valid_id_part1(id):
            checked_ids[id] = False
            sum_invalid_ids += int(id)
        else:
            checked_ids[id] = True

    print(f"expected test output: 1227775554 -- found: {sum_invalid_ids}")


def is_valid_id_part2(id: int) -> bool:
    windows = [window for window in range(1, len(id) // 2 + 1)]
    for window in windows:
        period = id[:window]
        if period * (len(id) // window) == id:
            return False
    return True


def solve_part2(ids: list[str]) -> int:
    sum_invalid_ids = 0
    checked_ids = defaultdict(bool)
    for id in ids:
        if id in checked_ids:
            if not checked_ids[id]:
                sum_invalid_ids += int(id)
            continue
        if not is_valid_id_part2(id):
            checked_ids[id] = False
            sum_invalid_ids += int(id)
        else:
            checked_ids[id] = True
    print(f"expected test output: 4174379265 -- found: {sum_invalid_ids}")


if __name__ == "__main__":
    parseInput("inputTest")
    solve_part1(all_ids_ranges)
    solve_part2(all_ids_ranges)
