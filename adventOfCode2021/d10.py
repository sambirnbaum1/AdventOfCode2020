from functools import reduce
from typing import Tuple, List, Union
from collections import Counter
from numpy import median

def check_line(line: str) -> Union[str, List[str]]:
    closer = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for c in line.strip():
        if c in closer:
            stack.append(closer[c])
        elif not stack or stack.pop() != c:
            return c
    return stack


def part1(input_: Tuple[str, ...]) -> int:
    char_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    corrupt_counter = Counter(filter(lambda result: isinstance(result, str), (check_line(line) for line in input_)))
    return sum(corrupt_counter[k] * v for k, v in char_score.items())


def part2(input_: Tuple[str, ...]) -> int:
    char_score = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in input_:
        missing = check_line(line)
        if isinstance(missing, str):
            continue
        scores.append(reduce(lambda part, close: part * 5 + char_score[close], reversed(missing), 0))
    return median(scores)


if __name__ == '__main__':
    with open('inputs/d10.txt', 'r') as fi:
        input_ = tuple(fi)
    print(part1(input_))
    print(part2(input_))

