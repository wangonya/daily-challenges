def narcissistic(n):
    n = str(n)
    digits = len(n)
    _sum = 0

    for digit in n:
        _sum += int(digit)**digits

    return int(n) == _sum


if __name__ == "__main__":
    assert narcissistic(153) is True
    assert narcissistic(1652) is False
