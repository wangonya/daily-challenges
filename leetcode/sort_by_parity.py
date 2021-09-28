from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if i % 2 == 0:
                if nums[i] % 2 != 0:
                    nums.append(nums.pop(i))
                else:
                    i += 1
            else:
                if nums[i] % 2 == 0:
                    nums.append(nums.pop(i))
                else:
                    i += 1
        return nums



s = Solution()
assert s.sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7]
