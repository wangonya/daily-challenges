from typing import List


def cyclic_rotation(a: List, k: int) -> List:
    # rotate a, k times
    if len(set(a)) < 2:
        # empty list or all duplicates
        return a

    # this approach doesn't work when k > len(a)
    # l = a[len(a) - k :]
    # a = l + a[: len(a) - k]
    # return a

    for _ in range(k):
        a.insert(0, a.pop())

    return a


assert cyclic_rotation([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert cyclic_rotation([1, 1, 2, 3, 5], 42) == [3, 5, 1, 1, 2]
