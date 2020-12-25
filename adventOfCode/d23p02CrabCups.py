from dataclasses import dataclass
from typing import Tuple, Iterator, Union

LEN = 1000000
MOVES = 10000000
INPUT = tuple(map(int, '284573961')) + tuple(range(10, LEN + 1))


def solve(vals: Tuple[int, ...] = INPUT) -> str:
    state = make_state(vals)
    for m in range(MOVES):
        if m % 100000 == 0:
            print(f'{m}, {m / MOVES}')
        update_state(state)
    return state.index[1].next.val * state.index[1].next.next.val


class StateNode: pass


@dataclass
class StateNode:
    val: int
    next: Union[None, StateNode] = None


@dataclass
class State:
    current: StateNode
    index: Tuple[StateNode, ...]


def join_nodes(first: StateNode, second: StateNode) -> None:
    first.next = second


def make_state_nodes(vals: Tuple[int, ...]) -> StateNode:
    current = StateNode(val=vals[0])
    prev = current
    for val in vals[1:]:
        state_node = StateNode(val=val)
        join_nodes(prev, state_node)
        prev = state_node
    join_nodes(prev, current)
    return current


def get_vals(current: StateNode) -> Iterator[int]:
    yield current.val
    node = current.next
    while node != current:
        yield node.val
        node = node.next


def make_index(node: StateNode) -> Tuple[StateNode, ...]:
    index = []
    while (node.val >= len(index)) or (not index[node.val]):
        while node.val >= len(index):
            index.append(None)
        index[node.val] = node
        node = node.next
    return tuple(index)


def make_state(vals: Tuple[int, ...]) -> State:
    current = make_state_nodes(vals)
    index = make_index(current)
    return State(current, index)


def update_state(state: State) -> State:
    current = state.current
    removed = [current.next]
    for _ in range(2):
        removed.append(removed[-1].next)

    join_nodes(current, removed[-1].next)

    removed_vals = {removed_cup.val for removed_cup in removed}
    destination_val = current.val
    while destination_val in removed_vals or destination_val == current.val:
        destination_val = ((destination_val - 2) % (len(state.index) - 1)) + 1

    destination = state.index[destination_val]

    join_nodes(removed[-1], destination.next)
    join_nodes(destination, removed[0])

    state.current = state.current.next
