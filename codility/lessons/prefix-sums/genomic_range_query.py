from typing import List


def solution(S: str, P: List[int], Q: List[int]) -> List[int]:
    impact = {"A": 1, "C": 2, "G": 3, "T": 4}
    result = []
    for a, b in zip(P, Q):
        result.append(impact[min(S[a:b + 1])])

    return result


assert solution("CAGCCTA", [2, 5, 0], [4, 5, 6]) == [2, 4, 1]
