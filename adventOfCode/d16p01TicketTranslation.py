import re
from itertools import chain
from .aocUtils import solver
from typing import Mapping, Tuple, Iterable, Iterator, FrozenSet

FILENAME = 'inputs/ticket_translation.txt'
RULE_PATTERN = re.compile(r'([\w\ ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')
Rules = Mapping[str, Tuple[Tuple[int, int], ...]]
TicketFilter = Tuple[FrozenSet[str], ...]


def parse_input(input_: Iterable[str]):
    iter_input = iter(input_)
    rules = parse_rules(iter_input)
    next(iter_input)
    my_ticket = parse_ticket(next(iter_input))
    next(iter_input)
    next(iter_input)
    other_tickets = list(map(parse_ticket, iter_input))
    return rules, my_ticket, other_tickets


@solver(FILENAME, str, transformer=parse_input)
def solve(input_):
    rules, my_ticket, other_tickets = input_
    filter_ = get_valid_filter(rules)
    return sum(chain(*(get_invalid_values(values, filter_) for values in other_tickets)))


def parse_ticket(ticket: str) -> Tuple[int]:
    return tuple(map(int, ticket.split(',')))


def parse_rules(input_: Iterator[str]) -> Rules:
    rules = dict()
    for line in input_:
        if line:
            name, lb1, ub1, lb2, ub2 = RULE_PATTERN.fullmatch(line).groups()
            rules[name] = ((int(lb1), int(ub1)), (int(lb2), int(ub2)))
        else:
            break
    return rules


def get_invalid_values(values: Iterable[int], filter_: TicketFilter) -> Iterable[int]:
    return (value for value in values if value >= len(filter_) or not filter_[value])


def get_valid_filter(rules: Rules) -> TicketFilter:
    global_ub = max(r[-1][-1] for r in rules.values())
    filter_ = [set() for _ in range(global_ub + 1)]
    for rule, ranges in rules.items():
        for i in chain(*(range(lb, ub + 1) for lb, ub in ranges)):
            filter_[i].add(rule)
    return tuple(map(frozenset, filter_))
