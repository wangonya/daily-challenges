# https://www.codewars.com/kata/5491689aff74b9b292000334

import re

repeated = re.compile(r"(.+?)\1+$")

def find_repeated_substring(s):
    match = repeated.match(s+s)
    substring = match.group(1)
    return (substring, s.count(substring))


assert find_repeated_substring('ababab') == ('ab', 3)
assert find_repeated_substring('abcde') == ('abcde', 1)
