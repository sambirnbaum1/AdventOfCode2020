from itertools import chain
from typing import Tuple, Iterable
import heapq

def part1(risks: Tuple[Tuple[int, ...], ...]) -> int:
    width, height = len(risks[0]), len(risks)
    target_x, target_y = target = width - 1, height - 1
    heap = [(0 + target_x + target_y, 0, (0, 0))]
    visited = {(0, 0)}
    while heap:
        _, cost, (x, y) = heapq.heappop(heap)
        for ax, ay in adj(x, y, width, height):
            if (ax, ay) in visited:
                continue
            visited.add((ax, ay))
            new_cost = cost + risks[ay][ax]
            est_cost = new_cost + target_x + target_y - x - y
            if (ax, ay) == target:
                return new_cost
            heapq.heappush(heap, (0, new_cost, (ax, ay)))


def part2(risks: Tuple[Tuple[int, ...], ...], rep: int = 5) -> int:
    extended_risks = tuple(
        tuple(
            tuple(chain.from_iterable((
                (cost + dx + dy - 1) % 9 + 1 for cost in row
            ) for dx in range(rep)))
            for dy in range(rep)
            for row in risks
        )
    )
    return part1(extended_risks)


def adj(x: int, y: int, width: int, height: int) -> Iterable[Tuple[int, int]]:
    return (
        (x, y)
        for x, y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        if 0 <= x < width and 0 <= y < height
    )

def parse_input(input_: Iterable[str]) -> Tuple[Tuple[int, ...], ...]:
    return tuple(tuple(int(value) for value in line.strip()) for line in input_)

if __name__ == '__main__':
    with open('inputs/d15.txt') as fi:
        risks = parse_input(fi)

    print(part1(risks))
    print(part2(risks))