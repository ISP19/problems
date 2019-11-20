def remove_vowel(string):
    """Remove all vowels in 'string', raise TypeError if 'string' is not str.
    >>> remove_vowel("abcdefg")
    "bcdfg"
    >>> remove_vowel("")
    ""
    >>> remove_vowel("AbCdeFg")
    "bCdFg"
    """
    new_string = ""
    vowel = "AEIOU"
    for s in string:
        if not((s in vowel) or (s in vowel.lower())):
            new_string += s
    return new_string