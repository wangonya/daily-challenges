from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        next_insert_pos = 1
        for i in range(n):
            nums.insert(next_insert_pos, nums.pop(n + i))
            next_insert_pos += 2

        return nums

    # fastest
    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n + i])
        return ans

    # least memory
    def shuffle3(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x, y in zip(nums[:n], nums[n:]):
            result.append(x)
            result.append(y)
        return result


s = Solution()
print(s.shuffle([2, 5, 1, 3, 4, 7], 3))
print(s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
