def tape_eq(A):
    total = sum(A)
    sum_so_far  = 0
    m = float('inf')

    for i in range(0, len(A)-1):
        n = A[i]
        sum_so_far += n
        diff = abs(sum_so_far - (total - sum_so_far))
        m = min(diff, m)

    print(m)
    return m

assert tape_eq([3, 1, 2, 4, 3]) == 1
assert tape_eq([1, 1, 3]) == 1
assert tape_eq([-1000, 1000]) == 2000
