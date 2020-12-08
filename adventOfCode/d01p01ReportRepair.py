import math
from typing import Collection

FILENAME = 'inputs/report_repair_input.txt'
TARGET = 2020


def solve(filename: str = FILENAME, target: int = TARGET) -> int:
    with open(filename, 'r') as fi:
        vals = set(map(int, fi))
    return find_vals(vals, target)


def find_vals(vals: Collection[int], target: int) -> int:
    assert pow(math.isqrt(target), 2) != target, 'Target can\'t be square'
    return next(val * (target - val)
                for val in vals if val in vals if target - val in vals)
