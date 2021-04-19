from itertools import permutations


def get_pin(observed):
    """
    ┌───┬───┬───┐
    │ 1 │ 2 │ 3 │
    ├───┼───┼───┤
    │ 4 │ 5 │ 6 │
    ├───┼───┼───┤
    │ 7 │ 8 │ 9 │
    └───┼───┼───┘
        │ 0 │
        └───┘
    """

    pin_observed = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }

    _len = len(observed)
    observed = ''.join(set(observed))

    if _len == 1:
        return pin_observed[observed]

    possible = []

    for n in observed:
        ps = list(''.join(p) for p in permutations(
            pin_observed[n], _len)
        )
        possible += ps

    for c in pin_observed[n]:
        possible.append(c * _len)

    print(sorted(possible))
    return sorted(possible)


if __name__ == "__main__":
    assert get_pin('1') == ['1', '2', '4']
    assert get_pin('7') == ['4', '7', '8']
    assert get_pin('2') == ['1', '2', '3', '5']
    assert get_pin('4') == ['1', '4', '5', '7']
    assert get_pin('8') == ['0', '5', '7', '8', '9']
    assert get_pin('5') == ['2', '4', '5', '6', '8']
    assert get_pin('6') == ['3', '5', '6', '9']
    assert get_pin('11') == sorted([
        "11",
        "22",
        "44",
        "12",
        "21",
        "14",
        "41",
        "24",
        "42"])
    x = sorted([
        '339',
        '366',
        '399',
        '658',
        '636',
        '258',
        '268',
        '669',
        '668',
        '266',
        '369',
        '398',
        '256',
        '296',
        '259',
        '368',
        '638',
        '396',
        '238',
        '356',
        '659',
        '639',
        '666',
        '359',
        '336',
        '299',
        '338',
        '696',
        '269',
        '358',
        '656',
        '698',
        '699',
        '298',
        '236',
        '239'])
    print(f"should be => {x}")
    assert get_pin('369') == sorted([
        "339",
        "366",
        "399",
        "658",
        "636",
        "258",
        "268",
        "669",
        "668",
        "266",
        "369",
        "398",
        "256",
        "296",
        "259",
        "368",
        "638",
        "396",
        "238",
        "356",
        "659",
        "639",
        "666",
        "359",
        "336",
        "299",
        "338",
        "696",
        "269",
        "358",
        "656",
        "698",
        "699",
        "298",
        "236",
        "239"])


# possible = [observed]
# observed = observed.split()
# # print(observed)

# for n in observed:
#     if int(n) % 3 == 0:
#         i = lock.index(n)
#         possible.append(lock[i - 1])
#         possible.append(lock[i + 3])
#         possible.append(lock[i - 3] if i != 2 else lock[i + 3])
#     elif int(n) % 2 == 0:
#         i = lock.index(n)
#         possible.append(lock[i + 1])
#         possible.append(lock[i + 3] if i != 7 else '0')
#         if i != 1:
#             possible.append(lock[i - 3])
#         if i != 3:
#             possible.append(lock[i - 1])
#     elif int(n) % 2 != 0 and int(n) not in (5, 0):
#         i = lock.index(n)
#         possible.append(lock[i + 1])
#         possible.append(lock[i + 3] if i == 0 else lock[i - 3])

# print(sorted(possible))
# return sorted(possible)
