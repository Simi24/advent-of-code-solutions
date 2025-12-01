from collections import defaultdict
from time import time

initial_secrets_numbers = []

with open("input.txt") as file:
    for line in file:
        initial_secrets_numbers.append(int(line.strip()))


def mix(secret_number, res):
    return secret_number ^ res


def prune(secret_number):
    return secret_number % 16777216


def step_1(secret_number):
    return prune(mix(secret_number, secret_number * 64))


def step_2(secret_number):
    return prune(mix(secret_number, secret_number // 32))


def step_3(secret_number):
    return prune(mix(secret_number, secret_number * 2048))


def get_next_secret_number(secret_number):
    return step_3(step_2(step_1(secret_number)))


def solve():
    time_start = time()
    sum = 0
    deltas = []
    for number in initial_secrets_numbers:
        prices = [number % 10]
        secret_number = number
        for i in range(0, 2000):
            secret_number = get_next_secret_number(secret_number)
            prices.append(secret_number % 10)
        changes = [(second - first, second) for first, second in zip(prices, prices[1:])]
        sum += secret_number
        deltas.append(changes)

    print(sum, round(time() - time_start))

    bananas = defaultdict(int)
    for changes in deltas:
        seen = set()
        for i in range(len(changes) - 3):
            sequence = tuple(change[0] for change in changes[i : i + 4])
            if sequence not in seen:
                bananas[sequence] += changes[i + 3][1]
                seen.add(sequence)

    print(max(bananas.values()), round(time() - time_start))


solve()
