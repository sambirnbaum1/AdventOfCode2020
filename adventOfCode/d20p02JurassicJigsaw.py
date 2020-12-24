from typing import Tuple, Iterable, Iterator, Mapping, Union
from .d20p01JurassicJigsaw import (FILENAME, get_edge_map, find_layout,
                                   get_configurations as get_tile_border_configurations,
                                   parse_tiles as parse_tile_border,
                                   Tile as TileBorder)
from itertools import chain, takewhile, product
from .aocUtils import solver
import re

Tile = Union[Tuple[str, ...], Iterable[str]]
SEA_MONSTER = (
'                  # ',
'#    ##    ##    ###',
' #  #  #  #  #  #   '
)



def parse_tiles(input_: Iterable[str]) -> Mapping[int, Tuple[str, ...]]:
    lines = iter(input_)
    tile_map = dict()
    try:
        while True:
            id_ = int(re.search(r'[0-9]+', next(lines)).group())
            tile = tuple(takewhile(lambda li: li, (li.strip() for li in lines)))
            tile_map[id_] = tile
    except StopIteration:
        return tile_map


def flip(tile: Tile) -> Tile:
    return tuple(row[::-1] for row in tile)


def rotate(tile: Tile, times: int) -> Tile:
    for _ in range(times % 4):
        tile = flip(map(''.join, zip(*tile)))
    return tile


def transform(tile: Tile, flipped, rotated):
    if flipped:
        tile = flip(tile)
    return rotate(tile, rotated)


def trim(tile: Tile):
    tile = tuple(row[1:-1] for row in tile)
    tile = tuple(tile[1:-1])
    return tile


@solver(FILENAME, str, tuple)
def solve(input_: Iterable[str]) -> int:

    tile_borders = tuple(parse_tile_border(input_))
    all_tile_border_configs = frozenset(chain(*map(get_tile_border_configurations, tile_borders)))
    top_map, left_map = (get_edge_map(all_tile_border_configs, side) for side in (0, 3))

    layout = find_layout(all_tile_border_configs, top_map, left_map)

    tile_map = parse_tiles(input_)

    tile_layout = {pos: transform(tile_map[border.id], border.flipped, border.rotated) for pos, border in layout.items()}
    width, height = max(tile_layout.keys())
    h = len(trim(next(iter(tile_layout.values()))))
    full_map = tuple(''.join(trim(tile_layout[(x, y)])[ty] for x in range(width+1)) for y in range(height+1) for ty in range(h))
    seamonster_spaces = seamonster_filter(full_map)

    return sum(char == '#' for row in full_map for char in row) - len(seamonster_filter(full_map))


def seamonster_filter(map_: Tuple[str,...]):

    def get_seamonster_configs():
        for flipped, rotated in product((True, False), range(4)):
            yield tuple(((x, y) for y, row in enumerate(transform(SEA_MONSTER, flipped, rotated)) for x, char in
                   enumerate(row) if char == '#'))

    def get_offset_seamonster(sea_moster: Tuple[Tuple[int, int], ...], d) -> Iterator[Tuple[int, int]]:
        dx, dy = d
        return ((x + dx, y + dy) for x, y in sea_moster)

    filter_ = frozenset()
    for seamonster in get_seamonster_configs():

        for d in product(range(len(map_)+10), repeat=2):
            offset_seamonster = tuple(get_offset_seamonster(seamonster, d))
            try:
                if all(map_[y][x] == '#' for x, y in offset_seamonster):
                    filter_ |= frozenset(offset_seamonster)
            except IndexError:
                pass
    return filter_
