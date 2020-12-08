from typing import Callable, Any, Iterable
import re
from .aocUtils import read_file_sections
from .d04p01PassportProcessing import parse_passport, FILENAME

HCL_PATTERN = re.compile(r'#[0-9a-f]{6}')
PID_PATTERN = re.compile(r'[0-9]{9}')
VALID_ECL = frozenset(('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))


RULES = {
    'byr': lambda byr: 1920 <= int(byr) <= 2002,
    'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
    'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
    'hgt': lambda hgt: (
        lambda val, unit: (
            (150 <= val <= 193 and unit == 'cm')
            or (56 <= val <= 76 and unit == 'in')
        )
    )(int(hgt[:-2]), hgt[-2:]),
    'hcl': HCL_PATTERN.fullmatch,
    'ecl': VALID_ECL.__contains__,
    'pid': PID_PATTERN.fullmatch
}


def solve(filename=FILENAME, rules=None):
    rules = rules or RULES
    with open(filename, 'r') as fi:
        cnt = count_valid(read_file_sections(fi), rules)
    return cnt


def count_valid(all_passport_data: Iterable[str], required_fields: dict[str, Callable[[str], Any]]):
    return sum(is_valid(parse_passport(pd), required_fields) for pd in all_passport_data)


def is_valid(passport: dict[str, str], rules: dict[str, Callable[[str], Any]]):
    try:
        return all(rule(passport[name]) for name, rule in rules.items())
    except (ValueError, KeyError):
        return False
