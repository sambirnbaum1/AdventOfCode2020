from functools import partial
from .aocUtils import prod
from .d03p01TobogganTrajectory import count_trees, FILENAME

DELTAS = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


def solve(filename=FILENAME, deltas=DELTAS):
    with open(filename, 'r') as fi:
        trees = fi.readlines()
    return prod(count_trees(trees, dx, dy) for dx, dy in deltas)


