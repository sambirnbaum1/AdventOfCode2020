from functools import lru_cache
from typing import Tuple, Mapping

from .d22p01CrabCombat import FILENAME, Deck, score_deck, parse_input
from .aocUtils import solver


@solver(FILENAME, str, parse_input)
def solve(decks: Mapping[str, Deck]) -> int:
    return score_deck(play_game(tuple(decks.values())))


def play_game(decks: Tuple[Deck, Deck]) -> Deck:

    #@lru_cache(maxsize=None)
    def play_subgame(deck1: Deck, deck2: Deck) -> Tuple[bool, Deck]:
        previous_states = set()
        player_2_wins = False
        while deck1 and deck2:
            if (deck1, deck2) in previous_states:
                return False, deck1
            previous_states.add((deck1, deck2))
            if all(len(deck) - 1 >= deck[0] for deck in (deck1, deck2)):
                player_2_wins, _ = play_subgame(deck1[1:deck1[0] + 1], deck2[1:deck2[0] + 1])
            else:
                player_2_wins = deck1 < deck2

            if player_2_wins:
                deck1, deck2 = deck1[1:], deck2[1:] + (deck2[0], deck1[0])
            else:
                deck1, deck2 = deck1[1:] + (deck1[0], deck2[0]), deck2[1:]

        return player_2_wins, (deck1, deck2)[player_2_wins]

    return play_subgame(*decks)[1]

