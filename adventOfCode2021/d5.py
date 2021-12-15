from itertools import groupby, chain, takewhile, count
from typing import Tuple, Iterable, Any, TypeVar, Callable, Iterator
import re
from collections import Counter


def get_points_from_line(start: complex, end: complex) -> Iterator[complex]:
    if end.real == start.real or end.imag == start.imag:
        dist = int(abs(end.real - start.real + end.imag - start.imag))
    else:
        dist = int(abs(end.real - start.real))
    direction = (end - start) / dist
    return (start + i * direction for i in range(dist + 1))


def part1(input_: Iterable[Tuple[complex, complex]]) -> int:
    return sum(
        1 for count in
        Counter(chain(*(
            get_points_from_line(start, end)
            for start, end in input_
            if start.real == end.real or start.imag == end.imag
        ))).values() if count > 1
    )

def part2(input_: Iterable[Tuple[complex, complex]]) -> int:
    return sum(
        1 for count in
        Counter(chain(*(
            get_points_from_line(start, end)
            for start, end in input_
        ))).values() if count > 1
    )


def parse_input(fstream: Iterable[str]) -> Tuple[Tuple[complex, complex], ...]:
    return tuple(
        (x1 + y1*1j, x2 + y2*1j)
        for x1, y1, x2, y2 in
        (((int(v) for v in re.findall(r'\d+', row)) for row in fstream))
    )


if __name__ == '__main__':
    with open('inputs/d5.txt') as fi:
        input_ = parse_input(fi)
    for line in input_:
        start, end = line
        print(line, line[0] - line[1])
        chain(takewhile(lambda p: p != end, (start + i * (end - start) for i in count())), (end,))
    print(part1(input_))
    print(part2(input_))
