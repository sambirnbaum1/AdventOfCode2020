from typing import Iterable

from .aocUtils import solver

FILENAME = 'inputs/combo_breaker.txt'
SUBJECT_NUMBER = 7
MODULO = 20201227
PUBLIC_KEY = 6270530


@solver(FILENAME, int)
def solve(vals: Iterable[int]):
    public_key1, public_key2 = vals
    loop_size1 = get_loop_size(SUBJECT_NUMBER, MODULO, public_key1)
    return pow(public_key2, loop_size1, MODULO)


def get_loop_size(subject_number: int, modulo: int, residue: int) -> int:
    for loop_size in range(1, modulo + 1):
        r = pow(subject_number, loop_size, modulo)
        if r == residue:
            return loop_size
