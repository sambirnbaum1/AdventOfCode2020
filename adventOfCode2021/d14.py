from functools import lru_cache, reduce
from operator import add
from typing import Tuple, Mapping, Iterable
from collections import Counter


def part1(template: str, rules: Mapping[str, str]) -> int:

    def insert_rules(template: str, rules: Mapping[str, str]):
        for c1, c2 in zip(template, template[1:]):
            yield c1
            segment = c1 + c2
            if segment in rules:
                yield rules[segment]
        yield c2

    for _ in range(10):
        template = ''.join(insert_rules(template, rules))
    counter = Counter(template)
    return max(counter.values()) - min(counter.values())


def part2(template: str, rules: Mapping[str, str]) -> int:

    @lru_cache(maxsize=None)
    def recurse(segment: str, depth: int) -> Counter:
        if depth == 0:
            return Counter()
        mid = rules[segment]
        return (
            recurse(segment[0] + mid, depth - 1)
            + recurse(mid + segment[1], depth - 1)
            + Counter(mid)
        )
    counts = (
        Counter(template)
        + reduce(add, (recurse(''.join(segment), 40) for segment in zip(template, template[1:])))
    )
    return max(counts.values()) - min(counts.values())





def parse_input(input_: Iterable[str]) -> Tuple[str, Mapping[str, str]]:
    template = next(input_).strip()
    next(input_)
    return (
        template,
        dict(line.strip().split(' -> ') for line in input_)
    )


if __name__ == '__main__':
    with open('inputs/d14.txt') as fi:
        template, rules = parse_input(fi)
    print(part1(template, rules))
    print(part2(template, rules))

