# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

from typing import List


def is_valid_walk(walk: List) -> bool:
    if len(walk) != 10:
        return False

    n_s = walk.count("n") == walk.count("s")
    e_w = walk.count("e") == walk.count("w")
    return n_s and e_w


if __name__ == "__main__":
    assert is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]) is True
    assert (
        is_valid_walk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"])
        is False
    )
    assert is_valid_walk(["w"]) is False
    assert is_valid_walk(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]) is False
    print("all good")

# from collections import Counter


# def isValidWalk(walk):
#     if len(walk) == 10:
#         walkmap = Counter(walk)
#         return walkmap["n"] == walkmap["s"] and walkmap["e"] == walkmap["w"]
#     return False
