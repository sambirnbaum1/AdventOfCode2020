from typing import Collection
from .d01p01ReportRepair import FILENAME, TARGET


def solve(filename: str = FILENAME, target: int = TARGET) -> int:
    with open(filename, 'r') as fi:
        vals = list(map(int, fi))
    return find_vals(vals, target)


def find_vals(vals: Collection[int], target: int) -> int:
    vals = sorted(vals)
    val_set = set(vals)
    for i, v1 in enumerate(vals):
        for j, v2 in enumerate(vals[i:]):
            v3 = target - v1 - v2
            if v3 <= v2 and (v2 != v3 or vals[j + 1] != v3):
                break
            if v3 in val_set:
                return v1 * v2 * v3
