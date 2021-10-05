from typing import List
class Solution:
    # Kadane's algorithm
    # 
    # Initializing max_till_now = 0
    # Initializing max_ending = 0
    # Repeat steps 4 to 6 for every element in the array
    # Set max_ending = max_ending + a[i]
    # if (max_ending<0) then set max_ending = 0
    # if (max_till_now < max_ending) then set max_till_now = max_ending
    # return max_till_now

    def maxSubArray(self, nums: List[int]) -> int:
        current_highest, overall_highest = float("-inf"), float("-inf") 
        for num in nums:
            current_highest = max(current_highest+num, num)
            overall_highest = max(overall_highest, current_highest)

        return overall_highest


s = Solution()
assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert s.maxSubArray([1]) == 1
assert s.maxSubArray([-1]) == -1
assert s.maxSubArray([5,4,-1,7,8]) == 23
