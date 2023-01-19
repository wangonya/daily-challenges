def solution(A):
    counter = 0
    zeros = 0

    for n in A:
        if n == 0:
            zeros += 1
        else:
            counter += zeros
        if counter > 1_000_000_000:
            return -1
    return counter


assert solution([0, 1, 0, 1, 1]) == 5
