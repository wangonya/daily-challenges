from typing import List


def solution(N: int, A: List[int]) -> List[int]:
    counters = [0 for _ in range(N)]
    max_counter = 0

    for n in A:
        if n <= N:
            counters[n-1] += 1
            max_counter = max(max_counter, counters[n-1])
        else:
            counters = [max_counter for _ in range(N)]
    return counters

assert solution(5, [3,4,4,6,1,4,4]) == [3, 2, 2, 4, 2]
