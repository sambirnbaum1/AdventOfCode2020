from typing import Mapping
from .d07p01HandyHaversacks import FILENAME, parse_rule, ORIGIN


def solve(filename: str = FILENAME) -> int:
    with open(filename, 'r') as fi:
        rule_map = dict(map(parse_rule, fi))
    return get_descendants(ORIGIN, rule_map)


def get_descendants(node: str, rule_map: Mapping[str, Mapping[str, int]]) -> int:
    bag_stack, descendants = [node], dict()
    while bag_stack:
        bag = bag_stack.pop()
        bag_rule = rule_map[bag]
        try:
            descendants[bag] = sum(qty * (1 + descendants[child])
                                   for child, qty in bag_rule.items())
        except KeyError:
            bag_stack.append(bag)
            bag_stack.extend(bag_rule.keys() - descendants.keys())
    return descendants[node]

