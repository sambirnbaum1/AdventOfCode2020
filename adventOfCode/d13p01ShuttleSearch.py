from typing import Iterable, Tuple
from .aocUtils import solver
from operator import mul


FILENAME = 'inputs/shuttle_search.txt'


@solver(FILENAME, str, tuple)
def solve(input_) -> int:
    time, busses = parse_input(input_)
    return mul(*get_next_time(time, busses))


def parse_input(input_):
    time = int(input_[0])
    busses = tuple(int(bus) for bus in input_[1].split(',') if bus != 'x')
    return time, busses


def get_next_time(time: int, busses: Iterable[int]) -> Tuple[int, int]:
    return min(map(lambda bus: (bus - (time % bus), bus), busses))

