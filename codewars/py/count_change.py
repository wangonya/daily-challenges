from typing import List


def count_change(money: int, coins: List):
    pass


if __name__ == "__main__":
    assert count_change(4, [1, 2]) == 3
    assert count_change(10, [5, 2, 3]) == 4
    assert count_change(11, [5, 7]) == 0
