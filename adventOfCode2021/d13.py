from collections import defaultdict
from functools import reduce
from itertools import takewhile
from typing import Tuple, Optional, Mapping, Iterable, Iterator
import re


def part1(page: Mapping[Tuple[int, int], int], folds: Tuple[Mapping[str, int]]) -> int:
    return sum(dotcount > 0 for dotcount in fold(page, **folds[0]).values())


def part2(page: Mapping[Tuple[int, int], int], folds: Tuple[Mapping[str, int]]) -> str:
    return render_page(reduce(lambda oldpage, fmap: fold(oldpage, **fmap), folds, page), 500, 500)


def fold(
        page: Mapping[Tuple[int, int], int],
        foldy: Optional[int] = None,
        foldx: Optional[int] = None
):
    newpage = defaultdict(int)
    for (x, y), count in page.items():
        newpage[
            x if foldx is None or x < foldx else 2 * foldx - x,
            y if foldy is None or y < foldy else 2 * foldy - y
        ] += count
    return newpage


def parse_input(input_: Iterable[str]) -> Tuple[Mapping[Tuple[int, int], int], Tuple[Mapping[str, int], ...]]:
    return {
        (int(x), int(y)): 1
        for x, y in (
            line.strip().split(',') for line in
            takewhile(
                str.strip,
                input_
            )
        )
    }, tuple(
        {f'fold{m.group(1)}': int(m.group(2))}
        for m in (
            re.match(r'fold along ([xy])=(\d+)', line)
            for line in input_
        )
    )


def render_page(page: Mapping[Tuple[int, int], int], width: int, height: int) -> str:
    return '\n'.join(
        ''.join('#' if page.get((x, y), 0) > 0 else '.' for x in range(width))
        for y in range(height)
    )


if __name__ == '__main__':
    with open('inputs/d13.txt', 'r') as fi:
        page, folds = parse_input(fi)
    print(part1(page, folds))
    print(part2(page, folds))

