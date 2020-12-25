from typing import Tuple

MOVES = 100
INPUT = tuple(map(int, '284573961'))


def solve(state: Tuple[int, ...] = INPUT, moves: int = MOVES) -> str:
    for _ in range(moves):
        state = next_state(state, 9)
    return ''.join(map(str, state))


def next_state(state: Tuple[int, ...], max_cup: int):
    removed = state[1:4]
    destination_cup = state[0]
    while destination_cup in removed or destination_cup == state[0]:
        destination_cup = ((destination_cup - 2) % max_cup) + 1
    destination_cup_index = state.index(destination_cup)
    return state[4:destination_cup_index + 1] + removed + state[destination_cup_index + 1:] + (state[0],)


