from .aocUtils import read_file_sections

FILENAME = 'inputs/custom_customs.txt'


def solve(filename=FILENAME):
    with open(filename, 'r') as fi:
        return sum(map(lambda section: len(set(section) - {'\n'}), read_file_sections(fi)))
