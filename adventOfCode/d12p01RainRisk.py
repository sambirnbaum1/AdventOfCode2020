from typing import Tuple, Iterable

from .aocUtils import solver
from dataclasses import dataclass
from functools import reduce

FILENAME = 'inputs/rain_risk.txt'
COS = {90: 0, 180: -1, 270: 0}
SIN = {90: 1, 180: 0, 270: -1}


@dataclass
class State:
    x: int
    y: int
    dir_x: int
    dir_y: int


def move(state: State, dx:int, dy:int) -> State:
    return State(state.x + dx, state.y + dy, state.dir_x, state.dir_y)


def rotate(state: State, degs: int) -> State:
    dir_x = state.dir_x * COS[degs] - state.dir_y * SIN[degs]
    dir_y = state.dir_x * SIN[degs] + state.dir_y * COS[degs]
    return State(state.x, state.y, dir_x, dir_y)


OPERATION_MAP = {
    'N': lambda v, state: move(state, 0, v),
    'S': lambda v, state: move(state, 0, -v),
    'E': lambda v, state: move(state, v, 0),
    'W': lambda v, state: move(state, -v, 0),
    'F': lambda v, state: move(state, v * state.dir_x, v * state.dir_y),
    'R': lambda v, state: rotate(state, 360 - v),
    'L': lambda v, state: rotate(state, v)
}


@solver(FILENAME, lambda op_str: (op_str[0], int(op_str[1:])))
def solve(operations: Iterable[Tuple[str, int]]):
    final_state = reduce(lambda state, op: OPERATION_MAP[op[0]](op[1], state), operations, State(0, 0, 1, 0))
    return abs(final_state.x) + abs(final_state.y)
