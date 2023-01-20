def solution(A, B, K):
    counter = 0

    for n in range(A, B + 1):
        if n % K == 0:
            counter += 1
    return counter


assert solution(6, 11, 2) == 3
assert solution(11, 345, 17) == 20
assert solution(0, 2_000_000_000, 1) == 2000000000
