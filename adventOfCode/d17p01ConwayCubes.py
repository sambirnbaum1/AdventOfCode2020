from typing import Tuple, Iterator, FrozenSet, Iterable
from itertools import product, chain
from .aocUtils import solver
from operator import add
from collections import Counter

ITERATIONS = 6
FILENAME = 'inputs/conway_cubes.txt'
DIMS = 3

Pos = Tuple[int, ...]


def get_initial_state(input_: Iterable[str], dims: int) -> Iterator[Pos]:
    return (
        (x, y) + (0,) * (dims - 2)
        for y, row in enumerate(input_) for x, cell in enumerate(row) if cell == '#'
    )


@solver(FILENAME, str)
def solve(input_: Iterator[str], dims=DIMS) -> int:
    state = frozenset(get_initial_state(input_, dims))
    for _ in range(ITERATIONS):
        state = frozenset(get_next_state(state))
    return len(state)


def get_adjacent(pos: Pos) -> Tuple[Pos, ...]:
    return tuple(tuple(map(add, pos, d)) for d in product((-1, 0, 1), repeat=len(pos)) if any(di != 0 for di in d))


def get_next_state(state: FrozenSet[Pos]) -> Iterator[Pos]:
    adjacent_count = Counter(chain(*map(get_adjacent, state)))
    return (pos for pos, count in adjacent_count.items() if count == 3 or (pos in state and count == 2))

