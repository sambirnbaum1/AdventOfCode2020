from .aocUtils import solver

FILENAME = 'inputs/adapter_array.txt'


@solver(FILENAME, int, sorted)
def solve(jolts):
    d1, d3 = map(sum, zip(*((j2 - j1 == 1, j2 - j1 == 3) for j1, j2 in zip([0] + jolts, jolts))))
    return d1 * (d3 + 1)