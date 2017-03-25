"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""


    letters_used = {letter.lower() for letter in sentence if letter.isalpha()}

    return len(letters_used) == 26



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
