from typing import Iterable
from functools import reduce
from operator import xor
from .d05p01BinaryBoarding import FILENAME, get_id


def solve(filename=FILENAME):
    with open(filename, 'r') as fi:
        return get_seat_id((li.strip() for li in fi))


def get_seat_id(seats: Iterable[str]) -> int:
    min_seat, max_seat, xor_seat = reduce(lambda mmx, seat_id:
                                          (min(mmx[0], seat_id),
                                           max(mmx[1], seat_id),
                                           mmx[2] ^ seat_id),
                                          map(get_id, seats),
                                          (float('inf'), -float('inf'), 0))
    return xor_seat ^ reduce(xor, range(min_seat, max_seat + 1))
