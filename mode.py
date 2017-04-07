"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    dictionary = {}
    result = set()

    for num in nums:
        dictionary[num] = dictionary.get(num, 0) + 1

    highest_count = max(dictionary.values())


    for item in dictionary:
        if dictionary[item] == highest_count:
            result.add(item)

    return result







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
