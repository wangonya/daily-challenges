from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TODO: make clearer
        p = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        print(output)
        p = 1
        for i in range(n - 1, -1, -1):
            print(f"i = {i}")
            output[i] = output[i] * p
            print(f"output = {output}")
            p = p * nums[i]
            print(f"p = {p}")
        return output
        # time limit exceeded
        # _len = range(1, len(nums) + 1)
        # answer = []
        # for i in _len:
        #     answer.append(math.prod(nums[: i - 1] + nums[i:]))
        # return answer


s = Solution()
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
# assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
