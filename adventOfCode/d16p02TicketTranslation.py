from typing import Tuple, Iterable, Iterator, Set, FrozenSet
from .d16p01TicketTranslation import parse_input, FILENAME, get_valid_filter, TicketFilter
from .aocUtils import solver, prod

Possibilities = Tuple[FrozenSet[str], ...]


@solver(FILENAME, str, transformer=parse_input)
def solve(input_):
    rules, my_ticket, other_tickets = input_
    filter_ = get_valid_filter(rules)
    possibilities = (get_possibilities(ticket, filter_) for ticket in filter_invalid(other_tickets, filter_))
    merged_possibilities = merge_possibilities(possibilities)
    configuration = search_possibilities(merged_possibilities)
    return prod(v for k, v in zip(configuration, my_ticket) if k.startswith('departure'))


def search_possibilities(merged_possibilities: Possibilities) -> Tuple[str]:
    traversal_order = sorted(((tuple(p), i) for i, p in enumerate(merged_possibilities)), key=lambda pi: len(pi[0]))

    def recurse(fields: Tuple[str, ...], used: Set[str]) -> Tuple[str, ...]:
        index = len(fields)
        if index == len(traversal_order):
            return fields
        possibilities, _ = traversal_order[index]
        for p in (p for p in possibilities if p not in used):
            new_configuration = recurse(fields + (p,), used | {p})
            if new_configuration:
                return new_configuration
        return tuple()

    return tuple(s for _, s in sorted((i, s) for (_, i), s in zip(traversal_order, recurse(tuple(), set()))))


def filter_invalid(tickets: Iterable[Tuple[int]], filter_: TicketFilter) -> Iterator[Tuple[int]]:
    return (ticket for ticket in tickets if is_valid(ticket, filter_))


def is_valid(ticket: Tuple[int], filter_: TicketFilter):
    return all(value < len(filter_) and filter_[value] for value in ticket)


def get_possibilities(ticket: Tuple[int], filter_: TicketFilter) -> Tuple[FrozenSet[str]]:
    return tuple(map(filter_.__getitem__, ticket))


def merge_possibilities(possibilities: Iterable[Possibilities]) -> Possibilities:
    return tuple(map(frozenset.intersection, *possibilities))
