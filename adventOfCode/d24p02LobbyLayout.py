from collections import Counter
from itertools import chain
from typing import Tuple, FrozenSet, Iterable

from .d24p01LobbyLayout import FILENAME, DIRECTIONS, DIRECTION_PATTERN
from .aocUtils import solver


@solver(FILENAME, DIRECTION_PATTERN.findall)
def solve(directions: Iterable[Tuple[str, ...]]) -> int:
    counter = Counter(sum(map(DIRECTIONS.__getitem__, direction)) for direction in directions)
    black_tiles = frozenset(tile for tile, cnt in counter.items() if cnt % 2)
    for _ in range(100):
        black_tiles = next_black_tiles(black_tiles)
    return len(black_tiles)


def get_adjacent(tile: complex):
    return (tile + d for d in DIRECTIONS.values())


def next_black_tiles(black_tiles: FrozenSet[complex]) -> FrozenSet[complex]:
    tile_hits = Counter(chain(*map(get_adjacent, black_tiles)))
    return frozenset(tile for tile, hits in tile_hits.items() if hits == 2 or (tile in black_tiles and hits == 1))
