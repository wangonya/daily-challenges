from collections import Counter
from typing import List


def odd_occurrences(a: List) -> int:
    n = (n for n, count in Counter(a).items() if count % 2 != 0)
    return next(n)


assert odd_occurrences([7, 3, 9, 3, 9, 9, 9]) == 7
