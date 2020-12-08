from typing import Iterable
import re

FILENAME = 'inputs/password_philosophy.txt'
INPUT_PATTERN = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')


def solve(filename: str = FILENAME):
    with open(filename, 'r') as fi:
        return count_valid(fi)


def count_valid(inputs: Iterable[str]) -> int:
    return sum(map(is_valid, inputs))


def is_valid(input_: str) -> bool:
    lb, ub, char, password = (cast(val)
                              for cast, val in zip((int, int, str, str), INPUT_PATTERN.match(input_).groups()))
    return lb <= password.count(char) <= ub
