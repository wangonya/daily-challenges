class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = False

        mp = {}

        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = t[i]
            print(mp.values())
            if len(mp.values()) > len(set(mp.values())):
                return False
            elif mp[s[i]] != t[i]:
                return False
            else:
                res = True
            print(mp)

        return res
            

s = Solution()
assert s.isIsomorphic("egg", "add") is True
assert s.isIsomorphic("foo", "bar") is False
assert s.isIsomorphic("paper", "title") is True
assert s.isIsomorphic("badc","baba") is False
assert s.isIsomorphic("egcd","adfd") is False
