class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        lh = len(haystack)
        if ln == 0:
            return 0
        for i in range(lh):
            if haystack[i:i+ln] == needle:
                return i
        return -1
