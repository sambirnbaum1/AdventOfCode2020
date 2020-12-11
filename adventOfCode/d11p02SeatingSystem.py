from itertools import product, count, takewhile
from typing import List, Iterator, Tuple, Mapping, Generator
from .aocUtils import solver
from .d11p01SeatingSystem import get_stable_state, FILENAME, SEAT_CHAR


MAX_NEIGHBORS = 4


@solver(FILENAME, list, list)
def solve(seats: List[List[str]], seat_char: str = SEAT_CHAR, max_neighbors: int = MAX_NEIGHBORS) -> int:
    dependencies = get_all_seat_dependencies(seats, seat_char)
    state = (False,) * len(dependencies)
    return sum(get_stable_state(state, dependencies, max_neighbors))


def get_all_seat_dependencies(seats: List[List[str]], seat_char: str) -> List[List[int]]:
    seat_map = dict()
    dependencies = []
    for pos, seat in (((row, col), seat) for row, seat_row in enumerate(seats) for col, seat in enumerate(seat_row)):
        if seat == seat_char:
            seat_map[pos] = seat_id = len(dependencies)
            dependencies.append([])
            for direction in get_directions(*pos):
                try:
                    dep_seat_id = next(seat_map[pos] for pos in direction if pos in seat_map)
                except StopIteration:
                    continue
                dependencies[dep_seat_id].append(seat_id)
                dependencies[seat_id].append(dep_seat_id)

    return dependencies


def get_directions(row: int, col: int) -> Iterator[Iterator[Tuple[int, int]]]:
    return (
        takewhile(lambda p: min(p) >= 0, ((row + drow * n, col + dcol * n) for n in count(1)))
        for drow, dcol in product((-1, 0), (-1, 0, 1))
        if (not drow == dcol == 0) and (drow == -1 or dcol < 1)
    )
