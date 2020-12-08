from typing import Collection, Iterable
import re
from .aocUtils import read_file_sections

FILENAME = 'inputs/passport_processing.txt'
REQUIRED_FIELDS = frozenset(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))

PASSPORT_PATTERN = re.compile(r'([a-z]{3}):([^\s]+)')


def solve(filename=FILENAME, required_fields=REQUIRED_FIELDS):
    with open(filename, 'r') as fi:
        return count_valid(read_file_sections(fi), required_fields)


def count_valid(all_passport_data: Iterable[str], required_fields: frozenset[str]):
    return sum(is_valid(parse_passport(pd), required_fields) for pd in all_passport_data)


def is_valid(passport: Collection[str], required_fields: frozenset[str]) -> bool:
    return required_fields.issubset(passport)


def parse_passport(passport_data: str) -> dict:
    return dict(PASSPORT_PATTERN.findall(passport_data))


