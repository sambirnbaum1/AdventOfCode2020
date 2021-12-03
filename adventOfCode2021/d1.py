from timeit import timeit
from typing import Tuple


def part1(input_: Tuple[int, ...]) -> int:
    return sum(1 for height1, height2 in zip(input_, input_[1:]) if height2 > height1)


def part2(input_: Tuple[int, ...]) -> int:
    return part1(tuple(sum(window) for window in zip(*(input_[start:] for start in range(3)))))


if __name__ == '__main__':
    with open('inputs/d1.txt', 'r') as fi:
        input_ = tuple(int(height) for height in fi)

    print(part1(input_))
    print(part2(input_))
