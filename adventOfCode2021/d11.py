from itertools import product, chain
from typing import Iterator, Tuple, List


def adj(x: int, y: int, width: int, height: int) -> Iterator[Tuple[int, int]]:
    return (
        (ax, ay) for ax, ay in (
            (x + dx, y + dy) for dx, dy in product((-1, 0, 1), (-1, 0, 1))
            if dx != 0 or dy != 0
        ) if 0 <= ax < width and 0 <= ay < height
    )


def next_state(state: List[List[int]]) -> int:
    width, height = len(state[0]), len(state)
    flash_count = 0
    flashes = set()
    for x, y in product(range(width), range(height)):
        octopus = state[y][x] = (state[y][x] + 1) % 10
        if octopus == 0:
            flashes.add((x, y))
    while flashes:
        flash_count += 1
        for x, y in adj(*flashes.pop(), width, height):
            octopus = state[y][x]
            if octopus == 9:
                state[y][x] = 0
                flashes.add((x, y))
            elif octopus > 0:
                state[y][x] += 1
    return flash_count


def part1(powers: Tuple[Tuple[int, ...], ...]) -> int:
    state = [list(row) for row in powers]
    flash_count = 0
    for _ in range(100):
        flash_count += next_state(state)
    return flash_count


def part2(powers: Tuple[Tuple[int, ...], ...]) -> int:
    state = [list(row) for row in powers]
    for i in range(1, 1000):
        next_state(state)
        if all(power == 0 for power in chain(*state)):
            return i

if __name__ == '__main__':
    with open('inputs/d11.txt', 'r') as fi:
        input_ = tuple(tuple(int(x) for x in row.strip()) for row in fi)
    print(part1(input_))
    print(part2(input_))
