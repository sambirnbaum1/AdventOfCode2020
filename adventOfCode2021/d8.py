from itertools import chain, permutations
from typing import Tuple, Iterable


def part1(mappings: Tuple[Tuple[Tuple[str, ...], Tuple[str, ...]], ...]) -> int:
    return sum(len(out) in {2, 4, 3, 7} for out in chain(*(out for _, out in mappings)))


def part2(mappings: Tuple[Tuple[Tuple[str, ...], Tuple[str, ...]], ...]) -> int:

    digits = {
        frozenset(key): value for
        value, key in enumerate(
            ('abcgef', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg')
        )
    }
    total = 0
    for ins, outs in mappings:
        remap = next(
            pmap for pmap in (dict(zip('abcdefg', p)) for p in permutations('abcdefg'))
            if all(frozenset(pmap[seg] for seg in in_) in digits for in_ in ins)
        )
        total += sum(10**(3 - i) * digits[frozenset(remap[seg] for seg in out)] for i, out in enumerate(outs))
    return total


def parse_input(input_: Iterable[str]) -> Tuple[Tuple[Tuple[str, ...], Tuple[str, ...]], ...]:
    return tuple((in_.split(), out.split()) for in_, out in (row.split('|') for row in input_))


if __name__ == '__main__':
    with open('inputs/d8.txt', 'r') as fi:
        mapping = parse_input(fi)
    print(part1(mapping))
    print(part2(mapping))
