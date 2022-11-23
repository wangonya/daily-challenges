def missing_el(a):
    total = sum(range(1,len(a)+2))
    return total - sum(a)


assert missing_el([2, 3, 1, 5]) == 4
# assert missing_el([]) == 0
assert missing_el([1]) == 2
