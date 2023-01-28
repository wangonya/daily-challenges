import math


def solution(A, B, K):
    start = math.ceil(A / K)
    end = math.floor(B / K)
    return end - start + 1


assert solution(6, 11, 2) == 3
assert solution(11, 345, 17) == 20
assert solution(0, 2_000_000_000, 1) == 2000000001
