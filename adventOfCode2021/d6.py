from collections import Counter
from itertools import chain
from typing import Tuple


def next_state(pops: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(chain(
        pops[1:7],
        (pops[0] + pops[7],),
        pops[8:],
        (pops[0],)
    ))


def solve(pops: Tuple[int, ...], days: int) -> int:
    for _ in range(days):
        pops = next_state(pops)
    return sum(pops)


def parse_input(input_: str):
    counts = Counter(int(age) for age in input_.split(','))
    return tuple(counts.get(age, 0) for age in range(9))


if __name__ == '__main__':
    with open('inputs/d6.txt') as fi:
        pops = parse_input(next(fi))
    print(solve(pops, 80))
    print(solve(pops, 256))