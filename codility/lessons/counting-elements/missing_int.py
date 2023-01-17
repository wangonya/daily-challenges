def solution(A):
    A = set(A)
    count = 1
    while count in A:
        count += 1
    return count

assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 3, 2]) == 4
assert solution([-1, -3]) == 1


