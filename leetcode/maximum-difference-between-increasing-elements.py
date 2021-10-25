from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff, min_num = -1, float("inf")
        for num in nums:
            min_num = min(num, min_num)
            max_diff = max(max_diff, num - min_num) 

        return max_diff or -1

s = Solution()
assert s.maximumDifference([7,1,5,4]) == 4
assert s.maximumDifference([9,4,3,2]) == -1
assert s.maximumDifference([1,5,2,10]) == 9
assert s.maximumDifference([87,68,91,86,58,63,43,98,6,40]) == 55
