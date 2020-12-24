import re
from typing import Iterator, Callable, Mapping
from operator import mul, add

from adventOfCode.aocUtils import solver

FILENAME = 'inputs/operation_order.txt'
TOKENS = re.compile('([0-9]+|[()+*])')
OPERATIONS = {
    '+': add,
    '*': mul
}


@solver(FILENAME, str)
def solve(expressions: Iterator[str]) -> int:
    return sum(map(evaluate_expression, expressions))


def evaluate_expression(expression: str, operations: Mapping[str, Callable[[int, int], int]] = OPERATIONS) -> int:
    stack = [0]
    op_stack = [add]
    for token in TOKENS.findall(expression):
        if token in operations:
            op_stack.append(operations[token])
        elif token == '(':
            stack.append(0)
            op_stack.append(add)
        elif token == ')':
            b, a = stack.pop(), stack.pop()
            stack.append(op_stack.pop()(a, b))
        else:
            stack.append(op_stack.pop()(stack.pop(), int(token)))
    return stack[-1]
