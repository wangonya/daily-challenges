class Solution:
    def climbStairs(self, n: int) -> int:
        prev, current = 0, 1
        for _ in range(n):
            print(f"prev = {prev}, current = {current}")
            prev, current = current, prev + current,
        return current 

s = Solution()
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
assert s.climbStairs(4) == 5
