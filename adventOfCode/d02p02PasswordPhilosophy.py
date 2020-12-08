from typing import Iterable
from .d02p01PasswordPhilosophy import FILENAME, INPUT_PATTERN


def solve(filename: str = FILENAME):
    with open(filename, 'r') as fi:
        return count_valid(fi)


def count_valid(inputs: Iterable[str]) -> int:
    return sum(map(is_valid, inputs))


def is_valid(input_: str) -> bool:
    p1, p2, char, password = (cast(val) for cast, val in
                              zip((int, int, str, str), INPUT_PATTERN.match(input_).groups()))
    v1, v2 = password[p1 - 1], password[p2 - 1]
    return v1 != v2 and char in (v1, v2)
