from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])


if __name__ == "__main__":
    s = Solution()
    assert s.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert s.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
