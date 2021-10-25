from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        duplicates = 0
        counter = 0

        while counter < nums_len:
            if nums[counter] == val:
                nums.pop(counter)
                nums.append(51)
                duplicates += 1
            else:
                counter += 1
        return len(nums[:nums_len-duplicates])

s = Solution()
assert s.removeElement([3,2,2,3], 3) == 2
assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5
        
