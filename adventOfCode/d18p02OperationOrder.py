from typing import Iterator, List
from .aocUtils import solver
from .d18p01OperationOrder import evaluate_expression, FILENAME, TOKENS


@solver(FILENAME, str)
def solve(expressions: Iterator[str]) -> int:
    return sum(map(evaluate_expression_new_oop, expressions))


def evaluate_expression_new_oop(exp: str) -> int:
    parenthesized_exp = ' '.join(parenthesize(exp))
    return evaluate_expression(parenthesized_exp)


def parenthesize(exp: str) -> List['str']:
    tokens = TOKENS.findall(exp)

    def parenthesize_side(seq):
        depth = 0
        for j, t in seq:
            if t == '(':
                depth += 1
            elif t == ')':
                depth -= 1
            if depth == 0:
                return j

    def parenthesize_at(i):
        p_left = parenthesize_side(zip(range(i - 1, -1, -1), tokens[i - 1:: -1]))
        p_right = parenthesize_side(enumerate(tokens[i + 1:], i + 2))
        return tokens[:p_left] + ['('] + tokens[p_left:p_right] + [')'] + tokens[p_right:]

    i = 0
    while i < len(tokens):
        if tokens[i] == '+':
            tokens = parenthesize_at(i)
            i += 1
        i += 1

    return tokens
