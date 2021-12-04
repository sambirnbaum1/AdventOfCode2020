from operator import mul, lt, ge
from typing import Tuple, Callable
from functools import reduce


def part1(input_: Tuple[str, ...]) -> int:
    return (lambda gamma: gamma * (gamma ^ ((1 << (gamma.bit_length())) - 1)))(reduce(
        lambda val, cnt: (val << 1) | (cnt >= len(input_) / 2),
        (sum(bit == '1' for bit in col) for col in zip(*input_)), 0
    ))


def part2(input_: Tuple[str, ...]) -> int:
    def select(candidates: Tuple[str, ...], i: int, choose1: Callable[[int, float], bool]):
        keep = '01'[choose1(sum(c[i] == '1' for c in candidates), len(candidates) / 2)]
        return (len(candidates) == 1 and candidates) or tuple(c for c in candidates if c[i] == keep)
    return mul(*(
        int(*reduce((lambda c, i: select(c, i, choose1)), range(len(input_[0])), input_), 2)
        for choose1 in (ge, lt)
    ))


if __name__ == '__main__':
    with open('inputs/d3.txt') as fi:
        input_ = tuple(li.strip() for li in fi)
    print(part1(input_))
    print(part2(input_))
