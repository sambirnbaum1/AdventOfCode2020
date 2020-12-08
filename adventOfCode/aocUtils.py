from typing import Iterable, Iterator, Generator
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



