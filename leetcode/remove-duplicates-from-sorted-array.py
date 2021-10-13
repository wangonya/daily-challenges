from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = None
        removed = 0
        nums_len = len(nums)
        for num in range(nums_len):
            if nums[-1-num+removed] == seen:
                nums.pop(nums_len-num)
                removed +=1
            seen = nums[-1-num+removed]
        print(nums)
        return len(nums)


s = Solution()
s.removeDuplicates([1,1,2]) == 2
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
