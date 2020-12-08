from .aocUtils import read_file_sections
from .d06p01CustomCustoms import FILENAME
from operator import and_
from functools import reduce


def solve(filename=FILENAME):
    with open(filename, 'r') as fi:
        return sum(map(len, (reduce(and_, map(set, section.split('\n'))) for section in read_file_sections(fi))))
