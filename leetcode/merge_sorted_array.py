from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        counter = 0
        while counter < n:
            nums1[m+counter] = nums2[counter]
            counter+=1

        nums1.sort()
        print(nums1)



s = Solution()
s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
s.merge([0],0,[1],1)
s.merge([0,0,0,0,0], 0, [1,2,3,4,5], 5)
