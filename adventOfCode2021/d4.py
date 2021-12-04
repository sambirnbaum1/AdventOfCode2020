from collections import defaultdict
from itertools import takewhile, chain
from typing import Tuple, Iterator

Board = Tuple[Tuple[int, ...], ...]


def part1(input_: Tuple[Tuple[int, ...], Tuple[Board, ...]]) -> int:
    return next(iter_win_scores(*input_))


def part2(input_: Tuple[Tuple[int, ...], Tuple[Board, ...]]) -> int:
    for score in iter_win_scores(*input_):
        pass
    return score


def parse_input(instream: Iterator[str]) -> Tuple[Tuple[int, ...], Tuple[Board, ...]]:
    sequence = tuple(int(v) for v in next(instream).split(','))
    next(instream)
    return sequence, tuple(tuple(
        tuple(int(v) for v in row.split()) for row in takewhile(str.strip, wstream)
    ) for wstream in (chain((row,), instream) for row in instream))


def iter_win_scores(sequence: Tuple[int, ...], boards: Tuple[Board, ...]) -> Iterator[int]:
    counter_map = defaultdict(lambda: [len(boards[0])])
    board_data = [
        ({
            value: (counter_map[board_n, 'r', row_n], counter_map[board_n, 'c', col_n])
            for row_n, row in enumerate(board) for col_n, value in enumerate(row)
        }, [0], board) for board_n, board in enumerate(boards)
    ]
    for v in sequence:
        for board_counter, score_pointer, board in tuple(board_data):
            try:
                row_counter, col_counter = board_counter[v]
            except KeyError:
                continue
            row_counter[0] -= 1
            col_counter[0] -= 1
            score_pointer[0] += v
            if not row_counter[0] or not col_counter[0]:
                board_data.remove((board_counter, score_pointer, board))
                yield v * (sum(chain(*board)) - score_pointer[0])


if __name__ == '__main__':
    with open('inputs/d4.txt', 'r') as fi:
        input_ = parse_input(fi)
    print(part1(input_))
    print(part2(input_))
