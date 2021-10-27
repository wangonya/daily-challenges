from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

s = Solution()
assert s.sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
assert s.sortColors([2,0,1]) == [0,1,2]
assert s.sortColors([0]) == [0]
assert s.sortColors([1]) == [1]