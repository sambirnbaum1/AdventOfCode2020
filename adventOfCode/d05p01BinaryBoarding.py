from functools import reduce

FILENAME = 'inputs/binary_boarding.txt'


def solve(filename=FILENAME):
    with open(filename, 'r') as fi:
        return max(map(lambda r: get_id(r.strip()), fi))


def get_id(seat: str) -> int:
    return reduce(lambda a, b: (a << 1) | (b in 'BR'), seat, 0)

