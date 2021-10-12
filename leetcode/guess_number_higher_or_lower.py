# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    if num == 6:
        return 0
    elif num < 6:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        pick = n
        upper_bound = n
        lower_bound = 0

        for _ in range(n):
            result = guess(pick)
            print(f"result = {result}")
            print(f"pick = {pick}")
            if result == 0:
                return pick
            elif result == 1:
                lower_bound = pick
                pick += (upper_bound - lower_bound) // 2
            elif result == -1:
                upper_bound = pick
                pick -= (upper_bound - lower_bound) // 2


s = Solution()
assert s.guessNumber(10) == 6
