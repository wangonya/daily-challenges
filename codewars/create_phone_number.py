def create_phone_number(n):
    a = ''.join([str(number) for number in n[:3]])
    b = ''.join([str(number) for number in n[3:6]])
    c = ''.join([str(number) for number in n[6:]])
    return f'({a}) {b}-{c}'


if __name__ == "__main__":
    assert create_phone_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
