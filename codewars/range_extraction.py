from itertools import groupby
from operator import itemgetter
from typing import List


def range_extraction(numbers: List) -> str:
    ranges = []

    # range = []
    # for i, n in enumerate(numbers):
    #     try:
    #         if n + 1 == numbers[i + 1]:
    #             if not range:
    #                 range.append(n)
    #             range.append(n + 1)
    #         elif len(range) >= 3:
    #             ranges.append(range)
    #             range = []
    #         else:
    #             range = []
    #     except IndexError:
    #         if len(range) >= 3:
    #             ranges.append(range)

    for i, g in groupby(enumerate(numbers), lambda x: x[0] - x[1]):
        group = map(itemgetter(1), g)
        group = list(group)
        if len(group) >= 3:
            ranges.append(f"{group[0]}-{group[-1]}")
        else:
            ranges.append(",".join(str(n) for n in group))

    ranges = ', '.join(str(n) for n in ranges).replace(' ', '')
    print(f"ranges = {ranges}")

    return ranges


if __name__ == "__main__":
    a = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7,
         8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    b = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]

    assert range_extraction(a) == '-6,-3-1,3-5,7-11,14,15,17-20'
    assert range_extraction(b) == '-3--1,2,10,15,16,18-20'
