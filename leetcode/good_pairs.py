#!/usr/bin/env python3
import collections
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = collections.defaultdict(int)
        count = 0
        # for every element in nums
        for num in nums:    
            # count number of pairs based on duplicate values
            count += repeat[num]
            # increment the number of counts
            repeat[num] += 1
            # number has not been seen before
        # return
        return count
if __name__ == '__main__':
    s = Solution()
    assert s.numIdenticalPairs([1,2,3,1,1,3]) == 4
