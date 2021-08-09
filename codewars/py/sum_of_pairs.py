# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python


def sum_of_pairs(ints, s):
    d = {}
    for n in ints:
        if s - n in d:
            return [d.get(s - n), n]
        d[n] = n


if __name__ == "__main__":
    assert sum_of_pairs([1, 4, 8, 7, 3, 15], 8) == [1, 7]
    assert sum_of_pairs([1, -2, 3, 0, -6, 1], -6) == [0, -6]

# def sum_pairs(lst, s):
#     cache = set()
#     for i in lst:
#         if s - i in cache:
#             return [s - i, i]
#         cache.add(i)
