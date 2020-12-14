from itertools import zip_longest, product

from .d14p01DockingData import FILENAME, PATTERN
from .aocUtils import solver
from typing import Iterator, Tuple, Generator


@solver(FILENAME, lambda s: PATTERN.match(s).groups())
def solve(operations: Iterator[Tuple[str, str]]) -> int:
    mask = None
    mem = dict()
    for ind, val in operations:
        if ind:
            for masked_ind in iter_masked_inds(int(ind), mask):
                mem[masked_ind] = int(val)
        else:
            mask = val
    return sum(mem.values())


def iter_masked_inds(ind: int, mask: str) -> Generator[int, None, None]:
    for x in map(list, product(*((True, False),) * mask.count('X'))):
        val = 0
        for i, m in zip_longest(bin(ind)[:1:-1], mask[::-1], fillvalue=0):
            if m == '1':
                val = (val << 1) | 1
            elif m == 'X':
                val = (val << 1) | x.pop()
            elif m == '0':
                val = (val << 1) | int(i)
        yield val
