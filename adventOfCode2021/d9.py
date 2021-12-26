from functools import reduce
from itertools import product
from operator import mul
from typing import Tuple, Iterable


def adj(x: int, y: int, width: int, height: int) -> Iterable[Tuple[int, int]]:
    return ((ax, ay) for ax, ay in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if 0 <= ax < width and 0 <= ay < height)


def part1(heights: Tuple[Tuple[int, ...], ...]):
    height, width = len(heights), len(heights[0])
    return sum(
        1 + heights[y][x]
        for x, y in product(range(width), range(height))
        if all(heights[y][x] < heights[ay][ax] for ax, ay in adj(x, y, width, height))
    )


def part2(heights: Tuple[Tuple[int, ...], ...]) -> int:
    height, width = len(heights), len(heights[0])
    basin_sizes = []
    visited = set()
    for location in product(range(width), range(height)):
        lx, ly = location
        if location in visited or heights[ly][lx] == 9:
            continue
        stack = [location]
        visited.add(location)
        size = 0
        while stack:
            x, y = stack.pop()
            size += 1
            next_locations = set((ax, ay) for ax, ay in adj(x, y, width, height) if heights[ay][ax] != 9) - visited
            stack.extend(next_locations)
            visited.update(next_locations)
        basin_sizes.append(size)
    return reduce(mul, sorted(basin_sizes, reverse=True)[:3])


if __name__ == '__main__':
    with open('inputs/d9.txt', 'r') as fi:
        heights = tuple(tuple(int(h) for h in row.strip()) for row in fi)
    print(part1(heights))
    print(part2(heights))