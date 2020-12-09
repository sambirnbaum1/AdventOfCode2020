from typing import Mapping, Iterable, List

FILENAME = 'inputs/encoding_error.txt'
WINDOW_SIZE = 25

def solve(filename=FILENAME):
    with open(filename, 'r') as fi:
        numbers = list(map(int, fi))
    return next(number
                 for number, window in iter_window(list(numbers), WINDOW_SIZE)
                 if not check_number(number, window))


def check_number(target: int, window: Mapping[int, int]):
    return any((target - key)
               in window and (target != key * 2 or cnt > 1)
               for key, cnt in window.items())



def iter_window(numbers: List[int], size):
    window = dict()


    def push(n: int):
        window[n] = window.get(n, 0) + 1


    def pop(n: int):
        window[n] -= 1
        if window[n] == 0:
            del window[n]

    for number in numbers[:size]:
        push(number)

    for first, next_ in zip(numbers, numbers[size:]):
        yield next_, window
        pop(first)
        push(next_)