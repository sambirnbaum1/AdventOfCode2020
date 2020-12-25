import re
from collections import Counter
from typing import Tuple, Iterable

from adventOfCode.aocUtils import solver

FILENAME = 'inputs/lobby_layout.txt'
DIRECTION_PATTERN = re.compile(r'(se|sw|ne|nw|e|w)')
DIRECTIONS = {
    'e': 1,
    'w': -1,
    'ne': 1j,
    'sw': -1j,
    'nw': 1j - 1,
    'se': 1 - 1j
}


@solver(FILENAME, DIRECTION_PATTERN.findall)
def solve(directions: Iterable[Tuple[str, ...]]) -> int:
    counter = Counter(sum(map(DIRECTIONS.__getitem__, direction)) for direction in directions)
    return sum(cnt % 2 for cnt in counter.values())

