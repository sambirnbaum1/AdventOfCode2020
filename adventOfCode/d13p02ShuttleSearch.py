from .aocUtils import solver
from typing import Iterator, Tuple
from .d13p01ShuttleSearch import FILENAME
from math import gcd


@solver(FILENAME, str, tuple)
def solve(input_: Tuple[str, str]) -> int:
    delta = 1
    time = 0
    for offset, bus in parse_input(input_[1]):
        while (time + offset) % bus:
            time += delta
        delta = int((delta * bus) / gcd(delta, bus))
    return time


def parse_input(input_: str) -> Iterator[Tuple[int, int]]:
    return ((i, int(bus)) for i, bus in enumerate(input_.split(',')) if bus != 'x')