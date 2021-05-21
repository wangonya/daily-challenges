import string


def rot13(message):
    """
    ROT13 is a simple letter substitution cipher that replaces
    a letter with the letter 13 letters after it in the alphabet.
    ROT13 is an example of the Caesar cipher.

    This function that takes a string and returns the string ciphered
    with Rot13. If there are numbers or special characters included
    in the string, they are returned as they are.
    """

    alph = string.ascii_lowercase
    new_str = ''

    for char in message:
        rot_13 = alph.find(char.lower())
        print(rot_13)
        if rot_13 != -1:
            rot_13 = alph.find(char.lower()) + 13
            rot_13 = rot_13 if rot_13 <= 25 else rot_13 - 26
            new_str += alph[rot_13].capitalize() \
                if char.isupper() else alph[rot_13]
        else:
            new_str += char

    return new_str


if __name__ == "__main__":
    assert rot13("test") == "grfg"
    assert rot13("Test") == "Grfg"

    print(rot13('10+2 is twelve.'))
    print(rot13('10+2 vf gjryir.'))
    print(rot13('Nibvq fhpprff ng nyy pbfgf!'))
