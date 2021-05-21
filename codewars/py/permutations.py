from itertools import permutations as ps


def permutations(s):
    p = set(''.join(p) for p in ps(s))
    return list(p)


if __name__ == "__main__":
    assert permutations('a') == ['a']
    assert permutations('ab') == ['ab', 'ba']
    assert permutations('aabb') == [
        'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
