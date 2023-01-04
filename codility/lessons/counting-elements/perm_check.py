def solution(A):
    A.sort()
    for i in range(len(A)-1):
        if A[i] - A[i+1] in (-1,0):
            continue
        return 0
    return 1

assert solution([4, 1, 3, 2]) == 1
assert solution([4, 1, 3]) == 0


# def solution(A):
#     # sum of first n natural numbers = n(n+1) / 2
#     n = max(A)
#     if sum(A) == (n * (n+1)) / 2:
#         return 1
#     return 0
