from itertools import count, islice
from typing import Iterable

FILENAME = 'inputs/toboggan_trajectory.txt'
ACROSS = 3
DOWN = 1


def solve(filename=FILENAME, across=ACROSS, down=DOWN):
    with open(filename, 'r') as fi:
        return count_trees(fi, across, down)


def count_trees(trees: Iterable[str], across: int, down: int) -> int:
    return sum(row[x % len(row)] == '#' for x, row in
               zip(count(0, across), (row.strip() for row in islice(trees, None, None, down))))
