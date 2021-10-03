from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i, n in enumerate(nums):
            if i > reachable:
                break
            reachable = max(reachable, i+n)

        return reachable >= len(nums) - 1


s = Solution()
assert s.canJump([2, 3, 1, 1, 4]) is True
assert s.canJump([3, 2, 1, 0, 4]) is False

# Time:  O(n)
# Space: O(1)
