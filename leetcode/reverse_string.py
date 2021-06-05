class Solution:
    def reverse(self, x: int) -> int:
        pos = x > 0

        x = str(abs(x))[::-1]
        x = int(x)

        print(f"x={x}")
        if x >= 2**31:
            return 0

        return x if pos else -x


s = Solution()
print(s.reverse(123456))
print(s.reverse(-123456))
print(s.reverse(1563847412))
