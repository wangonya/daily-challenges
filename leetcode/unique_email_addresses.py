import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            email = re.sub(r"\.", "", re.match(r"(.+?(?=@))", email).group(0))
            print(email)
        return len(unique_emails)

s = Solution()
assert s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
assert s.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]) == 3

# Solution
# Time:  O(n * l)
# Space: O(n * l)

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def convert(email):
            name, domain = email.split('@')
            name = name[:name.index('+')]
            return "".join(["".join(name.split(".")), '@', domain])

        lookup = set()
        for email in emails:
            lookup.add(convert(email))
        return len(lookup)
