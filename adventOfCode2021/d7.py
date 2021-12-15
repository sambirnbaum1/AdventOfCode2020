from typing import Tuple

from numpy import median


def part1(crabs: Tuple[int, ...]) -> int:
    median_crab = int(median(crabs))
    return sum(abs(median_crab - crab) for crab in crabs)


def part2(crabs: Tuple[int, ...]) -> int:
    start, end = min(crabs), max(crabs)
    costs = [0] * (end - start)
    for crab in crabs:
        for pos in range(start, end):
            delta = abs(pos - crab)
            costs[pos] += (delta * (delta + 1)) / 2
    return int(min(costs))


if __name__ == '__main__':
    with open('inputs/d7.txt') as fi:
        crabs = tuple(int(pos) for pos in next(fi).split(','))

    print(part1(crabs))
    print(part2(crabs))
