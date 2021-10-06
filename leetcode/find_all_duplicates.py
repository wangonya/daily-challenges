from typing import List
from collections import defaultdict


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x = defaultdict(int)
        
        for num in nums:
            x[num] += 1

        filtered_x = {k:v for (k,v) in x.items() if v == 2}
        return sorted(list(filtered_x.keys()))


s = Solution()
assert s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
assert s.findDuplicates([1, 1, 2]) == [1]
assert s.findDuplicates([1]) == []

# Time:  O(n)
# Space: O(n), this doesn't satisfy the question
from collections import Counter
class Solution3(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [elem for elem, count in Counter(nums).items() if count == 2]
