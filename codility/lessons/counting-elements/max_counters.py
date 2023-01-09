from typing import List


def solution(N: int, A: List[int]) -> List[int]:
    counters = [0] * N
    max_counter = 0
    start_line = 0

    for n in A:
        x = n - 1
        if n > N:
            start_line = max_counter
        elif counters[x] < start_line:
            counters[x] = start_line + 1
        else:
            counters[x] += 1

        if n <= N and counters[x] > max_counter:
            max_counter = max(max_counter, counters[n-1])
    for i in range(len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line
    print(counters)
    return counters

assert solution(5, [3,4,4,6,1,4,4]) == [3, 2, 2, 4, 2]
