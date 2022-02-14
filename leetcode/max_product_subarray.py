from typing import List


def max_product(nums: List[int]) -> int:
    prefix, suffix, max_so_far = 0, 0, float("-inf")
    for i in range(len(nums)):
        prefix = (prefix or 1) * nums[i]
        suffix = (suffix or 1) * nums[~i]  # https://stackoverflow.com/a/8305225/9312256
        max_so_far = max(max_so_far, prefix, suffix)
    return max_so_far


assert max_product([2, 3, -2, 4]) == 6
assert max_product([-2, 0, -1]) == 0
assert max_product([2, -5, -2, -4, 3]) == 24
