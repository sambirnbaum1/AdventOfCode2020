from typing import Iterator, Tuple
from .aocUtils import solver
import re
from functools import reduce
from dataclasses import dataclass


FILENAME = 'inputs/docking_data.txt'
PATTERN = re.compile(r'(?:mask|mem\[([0-9]+)\]) = ([0-9X]+)')


@solver(FILENAME, lambda s: PATTERN.match(s).groups())
def solve(operations: Iterator[Tuple[str, str]]) -> int:
    mask = None
    mem = dict()
    for ind, val in operations:
        if ind:
            mem[int(ind)] = apply_mask(int(val), mask)
        else:
            mask = parse_mask(val)
    return sum(mem.values())


@dataclass
class Mask:
    zeros: int
    ones: int


def parse_mask(mask: str) -> Mask:
    zeros = reduce(lambda zmask, b: (zmask << 1) | (b != '0'), mask, 0)
    ones = reduce(lambda omask, b: (omask << 1) | (b == '1'), mask, 0)
    return Mask(zeros=zeros, ones=ones)


def apply_mask(value: int, mask: Mask) -> int:
    return (value | mask.ones) & mask.zeros
