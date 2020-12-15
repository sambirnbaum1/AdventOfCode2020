from typing import Tuple
from .aocUtils import solver

FILENAME = 'inputs/rambunctious_recitation.txt'
NTURNS = 100


@solver(FILENAME, lambda li: tuple(map(int, li.split(','))), next)
def solve(numbers: Tuple[int], nturns=NTURNS) -> int:
    said = {val: index for index, val in enumerate(numbers[:-1])}
    last = numbers[-1]
    for turn in range(len(said), nturns - 1):
        say = turn - said[last] if last in said else 0
        said[last], last = turn, say
    return last
