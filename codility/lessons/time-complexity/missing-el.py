def missing_el(a):
    if not a:
        return 1
    if len(a) == 1:
        return 1 if a[0] == 2 else 2
    a = sorted(a)
    if a[0] != 1:
        return 1
    for i, n in enumerate(a, 1):
        if i != n:
            return i
    return a[-1] + 1


assert missing_el([2, 3, 1, 5]) == 4
assert missing_el([]) == 0
assert missing_el([1]) == 0
