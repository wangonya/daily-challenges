from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, num in enumerate(nums):
            diff = target - num
            if x.get(diff) != None:
                return [x.get(diff), i]
            x[num] = i

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [0,1]
assert s.twoSum([3,2,4], 6) == [1,2] 
assert s.twoSum([3,3], 6) == [0,1] 

