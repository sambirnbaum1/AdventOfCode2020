from functools import partial
from typing import Union, Tuple, Mapping, Any, Iterable
import re
from itertools import takewhile

from .aocUtils import solver

FILENAME = 'inputs/monster_message.txt'
Rule = Union[str, Tuple[Tuple[int, ...], ...]]


@solver(FILENAME, str)
def solve(input_):
    lines = iter(input_)
    rule_map = parse_rules(lines)
    rule_regex = to_regex(rule_map)
    return sum(bool(re.fullmatch(rule_regex, seq)) for seq in lines)


def parse_rules(rule_strs: Iterable[str]) -> Mapping[int, Rule]:
    return dict(map(parse_rule, takewhile(''.__ne__, rule_strs)))


def parse_rule(rule_str) -> Tuple[int, Union[str, Rule]]:
    key, rule = rule_str.split(': ')
    if re.match(r'"\w"', rule):
        return int(key), rule[1]
    return int(key), tuple(tuple(map(int, clause.split(' '))) for clause in rule.split(' | '))


def to_regex(rule_map: Mapping[int, Rule], max_depth=100) -> str:
    def recurse(rule_key: int, max_depth=max_depth):
        if not max_depth:
            return ''
        rule = rule_map[rule_key]
        if isinstance(rule, str):
            return rule
        return '({regex})'.format(regex='|'.join(''.join(map(partial(recurse, max_depth=max_depth - 1), clause)) for clause in rule))
    return recurse(0)
