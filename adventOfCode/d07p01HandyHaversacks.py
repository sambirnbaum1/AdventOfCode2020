from typing import Mapping, Iterable, Tuple, Set
from collections import defaultdict
import re

FILENAME = 'inputs/handy_haversacks.txt'
RULE_PATTERN = re.compile(r'(^|[0-9]+) ?(.*?) bags?')
ORIGIN = 'shiny gold'


def solve(filename: str = FILENAME) -> int:
    with open(filename, 'r') as fi:
        inverted_rules = invert_rules(map(parse_rule, fi))
    return len(get_all_ancestors(ORIGIN, inverted_rules))


def parse_rule(rule: str) -> Tuple[str, Mapping[str, int]]:
    parts = RULE_PATTERN.findall(rule)
    return parts[0][1], {bag: int(qty) for qty, bag in parts[1:]}


def invert_rules(rules: Iterable[Tuple[str, Mapping[str, int]]]) -> Mapping[str, Set[str]]:
    inverted_rules = defaultdict(set)
    for parent, child_qtys in rules:
        for child in child_qtys:
            inverted_rules[child].add(parent)
    return inverted_rules


def get_all_ancestors(node: str, inverted_rules: Mapping[str, Set[str]]) -> Set:
    bag_stack, ancestors = [node], {node}
    while bag_stack:
        bag = bag_stack.pop()
        new_ancestors = inverted_rules[bag] - ancestors
        ancestors.update(new_ancestors)
        bag_stack.extend(new_ancestors)
    return ancestors - {node}
