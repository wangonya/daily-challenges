# A permutation is a sequence containing each element from 1 to N once, and only once.
def solution(A):
    A.sort()
    if A[0] != 1:
        return 0
    for i in range(len(A)-1):
        if A[i] - A[i+1] == -1:
            continue
        return 0
    return 1

assert solution([2]) == 0
assert solution([4, 1, 3, 2]) == 1
assert solution([4, 1, 3]) == 0


# almost there - 83%. sum ok but not perm
# def solution(A):
#     # sum of first n natural numbers = n(n+1) / 2
#     n = max(A)
#     if sum(A) == (n * (n+1)) / 2:
#         return 1
#     return 0
