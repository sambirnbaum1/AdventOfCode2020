from .aocUtils import solver
from typing import Collection
from collections import defaultdict
from .d10p01AdapterArray import FILENAME


MAX_DELTA = 3


@solver(FILENAME, int, sorted)
def solve(jolts: Collection[int], max_delta: int = MAX_DELTA) -> int:
    ways_ending_in = defaultdict(int, {0: 1})
    for jolt in jolts:
        ways_ending_in[jolt] = sum(ways_ending_in[prev_jolt] for prev_jolt in range(jolt - max_delta, jolt))
    return ways_ending_in[jolts[-1]]
