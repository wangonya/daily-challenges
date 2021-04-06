from typing import List
from collections import Counter


def check_mag(magazine: List, note: List) -> str:
    match = (Counter(note) - Counter(magazine)) == {}
    # TOO SLOW:
    # match = False
    # for word in note:
    #     if word in mag:
    #         match = True
    #         mag.remove(word)
    #     else:
    #         match = False
    #         break

    return "Yes" if match else "No"


if __name__ == "__main__":
    assert check_mag(
        ['give', 'me', 'one', 'grand', 'today', 'night'],
        ['give', 'one', 'grand', 'today']) == "Yes"
    assert check_mag(
        ['two', 'times', 'three', 'is', 'not', 'four'],
        ['two', 'times', 'two', 'is', 'four']) == "No"
