from typing import Iterable, Iterator, Generator, Callable, TypeVar, Mapping, Any
from functools import reduce
from operator import mul
from itertools import takewhile


def prod(iter_: Iterable):
    return reduce(mul, iter_)


def read_file_sections(fi: Iterator[str]) -> Generator[str, None, None]:
    section = True
    while section:
        section = ''.join(takewhile(lambda li: li.strip(), fi)).strip()
        if section:
            yield section


Input = TypeVar('Input')
Return = TypeVar('Return')
SolverFn = Callable[[Iterable[Input], Mapping[str, Any]], Return]
SolverWrapper = Callable[[], Return]
SolverDecorator = Callable[[SolverFn], SolverWrapper]
Transformer = Callable[[Iterable[Input]], Iterable[Input]]


def solver(filename: str, type_: Callable[[str], Input],
           transformer: Transformer = lambda x: x) -> SolverDecorator:

    def decorator(fn: SolverFn) -> SolverWrapper:
        def wrapper(**kwargs) -> Return:
            with open(filename, 'r') as fi:
                return fn(transformer(map(type_, fi)), **kwargs)
        return wrapper
    return decorator


