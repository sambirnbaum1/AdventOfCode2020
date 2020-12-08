from dataclasses import dataclass
from typing import Tuple, Generator, Mapping, Callable
import re

FILENAME = 'inputs/handheld_halting.txt'

CMD_PATTERN = re.compile(r'([a-z]{3}) ([+-][0-9]+)')


@dataclass
class Command:
    kw: str
    val: int


@dataclass
class State:
    accumulator: int = 0
    ptr: int = 0


CommandMap = Mapping[str, Callable[[int, State], State]]

COMMAND_MAP = {
    'acc': lambda val, state: State(state.accumulator + val, state.ptr + 1),
    'nop': lambda val, state: State(state.accumulator, state.ptr + 1),
    'jmp': lambda val, state: State(state.accumulator, state.ptr + val)
}


def solve(filename=FILENAME):
    with open(filename, 'r') as fi:
        commands = tuple(map(parse_command, fi))

    visits = [False] * len(commands)
    for state in run_program(commands, COMMAND_MAP):
        if visits[state.ptr]:
            return state.accumulator
        visits[state.ptr] = True


def run_program(commands: Tuple[Command], command_map: CommandMap, state=State()) -> Generator[State, None, None]:

    while 0 <= state.ptr < len(commands):
        command = commands[state.ptr]
        state = get_next_state(state, command, command_map)
        yield state


def get_next_state(state: State, command: Command, command_map: CommandMap) -> State:
    return command_map[command.kw](command.val, state)


def parse_command(command_data: str) -> Command:
    kw, val = CMD_PATTERN.match(command_data).groups()
    return Command(kw, int(val))
