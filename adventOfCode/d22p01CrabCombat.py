from itertools import takewhile
from typing import Mapping, Tuple, Iterator
from .aocUtils import solver

FILENAME = 'inputs/crab_combat.txt'
Deck = Tuple[int, ...]


def parse_input(input_: Iterator[str]) -> Mapping[str, Deck]:
    return dict((next(input_)[:-1], tuple(map(int, takewhile(bool, input_)))) for _ in range(2))


@solver(FILENAME, str, parse_input)
def solve(decks) -> int:
    return score_deck(play_game(*decks.values()))


def play_game(deck1: Deck, deck2: Deck) -> Deck:

    def play_round(deck1: Deck, deck2: Deck) -> Tuple[Deck, Deck]:
        loser, winner = sorted((deck1, deck2))
        return winner[1:] + (winner[0], loser[0]), loser[1:]

    while deck1 and deck2:
        deck1, deck2 = play_round(deck1, deck2)

    return deck1


def score_deck(deck: Deck) -> int:
    return sum(i * v for i, v in enumerate(reversed(deck), 1))
