from typing import Iterator, Generator, Tuple, Mapping, List
from .d09p01EncodingError import FILENAME

TARGET = 85848519


def solve():
    with open(FILENAME, 'r') as fi:
        sequence = list(map(int, fi))
    return get_sum(TARGET, sequence)


def prefix_sum(sequence: Iterator[int]) -> Generator[Tuple[Mapping[int, int], int, int], None, None]:
    prefix = {0: 1}
    next_ = 0

    for i, s in enumerate(sequence):
        next_ += s
        yield prefix, next_, i
        prefix[next_] = i


def get_sum(target: int, sequence: List[int]) -> int:
    for prefix, next_, i in prefix_sum(sequence):
        if next_ - target in prefix and sequence[i] != target:
            subsequence = sequence[prefix[next_ - target]: i + 1]
            return min(subsequence) + max(subsequence)
