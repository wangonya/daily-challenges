def count_bits(n: int) -> int:
    b = f"{n:b}"
    return b.count("1")


if __name__ == "__main__":
    assert count_bits(0) == 0
    assert count_bits(4) == 1
    assert count_bits(7) == 3
    assert count_bits(9) == 2
    assert count_bits(10) == 2
