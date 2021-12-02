from typing import Iterable, Tuple
from itertools import accumulate
from functools import reduce

DIRECTIONS = {'forward': 1, 'down': 1j, 'up': -1j}
AIM_DIRECTIONS = {'down': 1, 'up': -1}


def parse_input(input_: Iterable[str]) -> Iterable[Tuple[str, int]]:
    return ((lambda dir_, dis: (dir_, int(dis)))(*inst.split(' ')) for inst in input_)


def prod_part(i: int) -> int:
    return int(i.real * i.imag)


def part1(input_: Iterable[str]) -> int:
    return prod_part(sum(dis * DIRECTIONS[dir_] for dir_, dis in parse_input(input_)))


def part2(input_: Iterable[str]) -> int:
    return prod_part(reduce(
        lambda a, b: a + (b[0] == 'forward') * b[1] * (1 + b[2]*1j),
        accumulate(
            parse_input(input_),
            (lambda last, inst: (*inst, last[2] + AIM_DIRECTIONS.get(inst[0], 0) * inst[1])), initial=(0, 0, 0)
        ), 0
    ))


if __name__ == '__main__':
    with open('inputs/d2.txt', 'r') as fi:
        input_ = tuple(fi)

    print(part1(input_))
    print(part2(input_))

