from collections import Counter


def two_strings(s1: str, s2: str) -> str:
    x = Counter(s1)
    y = Counter(s2)
    return "YES" if x.keys() & y.keys() else "NO"


if __name__ == "__main__":
    # assert two_strings("hello", "world") == "YES"
    assert two_strings("hi", "world") == "NO"
