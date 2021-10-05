from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return len(nums_set) < len(nums)

s = Solution()
assert s.containsDuplicate([1,2,3,1]) is True
assert s.containsDuplicate([1,2,3,4]) is False
assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) is True
