def valid_parens(s: str) -> bool:
    opening = '[({'
    closing = '])}'

    brackets = []

    for bracket in s:
        if bracket in opening:
            brackets.append(opening.index(bracket))
        elif brackets and brackets[-1] == closing.index(bracket):
            del brackets[-1]
        else:
            return False

    return True and brackets == []


if __name__ == '__main__':
    assert valid_parens("([)])") == False
    assert valid_parens("()") == True
    assert valid_parens("([)]") == False
