from typing import Iterable, Tuple
from functools import reduce
from .aocUtils import solver
from .d12p01RainRisk import FILENAME, State, move, rotate


def move_waypoint(state, dx, dy):
    return State(state.x, state.y, state.dir_x + dx, state.dir_y + dy)


OPERATION_MAP = {
    'N': lambda v, state: move_waypoint(state, 0, v),
    'S': lambda v, state: move_waypoint(state, 0, -v),
    'E': lambda v, state: move_waypoint(state, v, 0),
    'W': lambda v, state: move_waypoint(state, -v, 0),
    'F': lambda v, state: move(state, v * state.dir_x, v * state.dir_y),
    'R': lambda v, state: rotate(state, 360 - v),
    'L': lambda v, state: rotate(state, v)
}


@solver(FILENAME, lambda op_str: (op_str[0], int(op_str[1:])))
def solve(operations: Iterable[Tuple[str, int]]):

    final_state = reduce(lambda state, op: OPERATION_MAP[op[0]](op[1], state), operations, State(0, 0, 10, 1))
    return abs(final_state.x) + abs(final_state.y)