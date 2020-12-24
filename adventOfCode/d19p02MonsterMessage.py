from functools import lru_cache, reduce
from itertools import chain
from random import shuffle
from typing import Mapping, Tuple, Generator
from .aocUtils import solver
from .d19p01MonsterMessage import parse_rules, FILENAME, Rule

RULE_OVERRIDE = {
    8: ((42,), (42, 8)),
    11: ((42, 31), (42, 11, 31))
}
test_input = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''.split('\n')



@solver(FILENAME, str)
def solve(input_):
    lines = iter(input_)
    #rule_map = parse_rules(lines)
    rule_map = {**parse_rules(lines), **RULE_OVERRIDE}
    #for seq in lines:
    #    if matches_rules(rule_map, seq):
    #        print(seq)
    return sum(matches_rules(rule_map, string) for string in lines)



def matches_rules(rule_map: Mapping[int, Rule], seq: str) -> bool:

    @lru_cache(maxsize=None)
    def recurse(rule_index: int, seq_index) -> Tuple[int, ...]:
        rule = rule_map[rule_index]
        if isinstance(rule, str):
            if seq_index < len(seq) and rule == seq[seq_index]:
                return seq_index + 1,
            else:
                return tuple()
        else:
            next_indexes = tuple()
            for clause in rule:
                indexes = (seq_index,)
                for rule_index2 in clause:
                    indexes = chain(*(recurse(rule_index2, i) for i in indexes))
                next_indexes = (*next_indexes, *indexes)
            return next_indexes
    return any(str_index == len(seq) for str_index in recurse(0, 0))
