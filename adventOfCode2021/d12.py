from collections import defaultdict
from typing import Iterable, Mapping, List, FrozenSet


def part1(graph: Mapping[str, List[str]]) -> int:
    def dfs(node: str, small_visited: FrozenSet) -> int:
        if node == 'end':
            return 1
        return sum(
            dfs(
                next_node,
                small_visited | (set() if node.upper() == node else {node}))
            for next_node in graph[node] if next_node not in small_visited)
    return dfs('start', frozenset({'start'}))


def part2(graph: Mapping[str, List[str]]) -> int:
    def dfs(node: str, small_visited: FrozenSet, twice: bool, path) -> int:
        if node == 'end':
            return 1
        return sum(
            dfs(
                next_node,
                small_visited | (set() if node.upper() == node else {node}),
                twice or (next_node in small_visited),
                path + (next_node,)
            )
            for next_node in graph[node]
            if next_node != 'start' and (next_node not in small_visited or not twice)
        )
    return dfs('start', frozenset({'start'}), False, ('start',))




def parse_input(input_: Iterable[str]) -> Mapping[str, List[str]]:
    mapping = defaultdict(list)
    for edge in input_:
        a, b = edge.strip().split('-')
        mapping[a].append(b)
        mapping[b].append(a)
    return mapping


if __name__ == '__main__':
    with open('inputs/d12.txt', 'r') as fi:
        graph = parse_input(fi)
    print(part1(graph))
    print(part2(graph))