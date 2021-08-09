# https://www.codewars.com/kata/548db0bd1df5bbf29b0000b7/train/python
import re

pattern = re.compile()
valid_date = ""

assert valid_date.search("[01-23]") != None
assert valid_date.search("[02-31]") == None
assert valid_date.search("[[[08-29]]]") != None
assert valid_date.search("[13-02]") == None
assert valid_date.search("[02-[08-11]04]") != None
assert valid_date.search("ignored [08-11] ignored") != None

# solution
months_30 = "(04|06|09|11)"
months_31 = "(01|03|05|07|08|10|12)"
months_28 = "02"
days_30 = "(0[1-9]|[1-2][0-9]|30)"
days_31 = "(0[1-9]|[12][0-9]|3[01])"
days_28 = "(0[1-9]|1[0-9]|2[0-8])"
valid_date = re.compile(
    "\[(%s-%s|%s-%s|%s-%s)\]"
    % (months_30, days_30, months_31, days_31, months_28, days_28)
)
