from itertools import product
from typing import List, Iterator, Tuple, Mapping, Generator
from .aocUtils import solver

FILENAME = 'inputs/seating_system.txt'
SEAT_CHAR = 'L'
MAX_NEIGHBORS = 3


@solver(FILENAME, list, list)
def solve(seats: List[List[str]], seat_char: str = SEAT_CHAR, max_neighbors: int = MAX_NEIGHBORS) -> int:
    dependencies = get_all_seat_dependencies(seats, seat_char)
    for d in enumerate(dependencies):
        print(*d)
    state = (False,) * len(dependencies)
    return sum(get_stable_state(state, dependencies, max_neighbors))


def get_stable_state(state: Tuple[str], dependencies: List[List[int]], max_neighbors: int) -> Tuple[str]:
    visited_states = set()
    last_state = None
    while last_state != state:
        if state in visited_states:
            raise RuntimeError('Looping')
        visited_states.add(state)
        last_state, state = state, get_next_state(state, dependencies, max_neighbors)
    return state


def get_next_state(state: Tuple[bool], dependencies: List[List[int]],
                   max_neighbors: int) -> Tuple[bool]:
    return tuple(not (seat or any(map(state.__getitem__, seat_dependencies)))
                 or (seat and sum(map(state.__getitem__, seat_dependencies)) <= max_neighbors)
                 for seat, seat_dependencies in zip(state, dependencies))


def get_all_seat_dependencies(seats: List[List[str]], seat_char: str) -> List[List[int]]:
    seat_map = dict()
    dependencies = []
    for pos, seat in (((row, col), seat) for row, seat_row in enumerate(seats) for col, seat in enumerate(seat_row)):
        if seat == seat_char:
            seat_map[pos] = seat_id = len(dependencies)
            dependencies.append([])
            for dep_seat_id in (seat_map[pos] for pos in get_prev_adjacent(*pos) if pos in seat_map):
                dependencies[dep_seat_id].append(seat_id)
                dependencies[seat_id].append(dep_seat_id)
    return dependencies


def get_prev_adjacent(row: int, column: int) -> Iterator[Tuple[int, int]]:
    return ((row + drow, column + dcol)
            for drow, dcol in product((-1, 0), (-1, 0, 1))
            if (not drow == dcol == 0) and (drow == -1 or dcol < 1))

