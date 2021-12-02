from typing import Iterable, Tuple
from itertools import accumulate
from functools import reduce

DIRECTIONS = {'forward': 1, 'down': 1j, 'up': -1j}
AIM_DIRECTIONS = {'down': 1, 'up': -1}


def parse_input(input_: Iterable[str]) -> Iterable[Tuple[str, int]]:
    return ((lambda dir_, dis: (dir_, int(dis)))(*inst.split(' ')) for inst in input_)


def part1(input_: Iterable[str]) -> int:
    return (lambda i: int(i.real * i.imag))(sum(dis * DIRECTIONS[dir_] for dir_, dis in parse_input(input_)))


def part2(input_: Iterable[str]) -> int:
    parsed_input = tuple(parse_input(input_))
    aims = accumulate(parsed_input, (lambda aim, inst: aim + AIM_DIRECTIONS.get(inst[0], 0) * inst[1]), initial=0)
    x = reduce(
        lambda a, b: a + (b[0] == 'forward') * b[1] * (1 + b[2]*1j),
        ((*inst, aim) for inst, aim in zip(parsed_input, aims)), 0
    )
    return int(x.real * x.imag)


if __name__ == '__main__':
    with open('inputs/d2.txt', 'r') as fi:
        input_ = tuple(fi)

    print(part1(input_))
    print(part2(input_))

