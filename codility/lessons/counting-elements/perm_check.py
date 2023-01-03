def solution(A):
    # sum of first n natural numbers = n(n+1) / 2
    n = max(A)
    if sum(A) == (n * (n+1)) / 2:
        return 1
    return 0

assert solution([4, 1, 3, 2]) == 1
assert solution([4, 1, 3]) == 0
