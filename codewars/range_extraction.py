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

# enumerate takes an iterable and returns a sequence of pairs where the
# first element is the index in the iterable, and the second is the value

# e.g. enumerate([1, 4, 5, 6, 9]) returns ((0,1), (1,4), (2,5), (3,6), (4,9)).

# If a set of numbers belong to a sequence, their value minus their index should all be the same (assuming the numbers are sorted). So using the previous example:
# [i for i in map(lambda p: p[1]-p[0], enumerate([1,4,5,6,9]))] returns [1, 3, 3, 3, 5].

# groupby combines all entries with the same key (in this case, the result of the lambda expression):
# [[j for j in i[1]] for i in groupby(enumerate([1,4,5,6,9]), lambda p: p[1]-p[0])] returns [[(0, 1)], [(1, 4), (2, 5), (3, 6)], [(4, 9)]]
