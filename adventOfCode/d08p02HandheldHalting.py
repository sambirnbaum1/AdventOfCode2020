from typing import Tuple
from .d08p01HandheldHalting import (FILENAME, parse_command, COMMAND_MAP, State,
                                    run_program, Command, CommandMap, get_next_state)


ALTERNATE_COMMAND_MAP = {
    'nop': COMMAND_MAP['jmp'],
    'jmp': COMMAND_MAP['nop']
}


def solve(filename=FILENAME):
    with open(filename, 'r') as fi:
        commands = tuple(map(parse_command, fi))
    return fix_program(commands, COMMAND_MAP, ALTERNATE_COMMAND_MAP)


def fix_program(commands: Tuple[Command], command_map: CommandMap, alternate_command_map: CommandMap) -> int:

    state = State()
    bad_ptrs = [False] * len(commands)

    def check_program(test_state: State) -> Tuple[bool, int]:
        for test_state in run_program(commands, COMMAND_MAP, test_state):
            if test_state.ptr == len(commands):
                return True, test_state.accumulator
            if test_state.ptr > len(commands) or test_state.ptr < 0 or bad_ptrs[test_state.ptr]:
                return False, test_state.accumulator
            bad_ptrs[test_state.ptr] = True

    for _ in commands:
        command = commands[state.ptr]
        if command.kw in alternate_command_map:
            outcome, accumulator = check_program(get_next_state(state, command, alternate_command_map))
            if outcome:
                return accumulator
        state = command_map[command.kw](command.val, state)

    print('Unsolvable')




