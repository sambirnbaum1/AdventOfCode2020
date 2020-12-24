from collections import defaultdict
from typing import Tuple, Iterable, Iterator, Mapping, Set, FrozenSet, Union
import re
from .aocUtils import solver, prod
from dataclasses import dataclass, replace
from itertools import takewhile, chain, product

FILENAME = 'inputs/jurassic_jigsaw.txt'

@dataclass(eq=True, frozen=True)
class Tile:
    id: int
    sides: Tuple[Tuple[bool, ...], Tuple[bool, ...], Tuple[bool, ...], Tuple[bool, ...]]
    flipped: bool = False
    rotated: int = 0


def parse_tiles(input_: Iterable[str]) -> Iterator[Tile]:
    lines = iter(input_)
    try:
        while True:
            id_ = int(re.search(r'[0-9]+', next(lines)).group())
            tile = tuple(tuple(map('#'.__eq__, li)) for li in takewhile(lambda li: li.strip(), lines))
            tile_transpose = tuple(zip(*tile))
            yield Tile(id=id_, sides=(tile[0], tile_transpose[-1], tuple((tile[-1])), tuple((tile_transpose[0]))))
    except StopIteration:
        pass


def rotate(tile: Tile):
    top, left, bottom, right = tile.sides
    return replace(tile,
                   rotated=(tile.rotated + 1) % 4,
                   sides=(tuple(reversed(right)), top, tuple(reversed(left)), bottom))


def flip(tile: Tile):
    top, left, bottom, right = tile.sides
    return replace(tile,
                   flipped=not tile.flipped,
                   sides=(tuple(reversed(top)), right, tuple(reversed(bottom)), left))


def get_configurations(tile: Tile):
    transformed = tile
    for _ in range(2):
        for _ in range(4):
            yield transformed
            transformed = rotate(transformed)

        transformed = flip(tile)


def get_edge_map(tiles: Iterable[Tile], side: int) -> Mapping[Tuple[bool, ...], FrozenSet[Tile]]:
    mapping = defaultdict(frozenset)
    for tile in tiles:
        mapping[tile.sides[side]] |= {tile}
    return mapping


@solver(FILENAME, str, parse_tiles)
def solve(tiles: Tuple[Tile]) -> int:
    all_tile_configs = frozenset(chain(*map(get_configurations, tiles)))
    top_map, left_map = (get_edge_map(all_tile_configs, side) for side in (0, 3))

    layout = find_layout(all_tile_configs, top_map, left_map)

    width, height = max(layout.keys())
    return prod(layout[pos].id for pos in product((0, width), (0, height)))


def find_layout(tiles: FrozenSet[Tile],
                top_map: Mapping[Tuple[bool, ...], FrozenSet[Tile]],
                left_map: Mapping[Tuple[bool, ...], FrozenSet[Tile]]):
    height = width = int(pow(len(tiles)//8, .5))

    def get_fit(cell: Tuple[int, int],
                layout: Mapping[Tuple[int, int], Tile],
                used_tiles: Set[int]) -> Iterable[Tile]:
        x, y = cell
        above = left = tiles
        if y > 0:
            above = top_map[layout[(x, y - 1)].sides[2]]
        if x > 0:
            left = left_map[layout[(x - 1, y)].sides[1]]

        return (tile for tile in (above & left) if tile.id not in used_tiles)

    def recurse(cell: Tuple[int, int],
                layout: Mapping[Tuple[int, int], Tile],
                used_tiles: Set[int]) \
            -> Union[None, Mapping[Tuple[int, int], Tile]]:
        x, y = cell
        if y == height:
            return layout

        next_cell = ((x + 1) % width, y + (x + 1) // width)
        for tile in get_fit(cell, layout, used_tiles):
            final_layout = recurse(next_cell, {**layout, **{cell: tile}}, used_tiles | {tile.id})
            if final_layout:
                return final_layout
        return None

    return recurse((0, 0), dict(), set())
