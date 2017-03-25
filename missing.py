"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10, 8], 10)
    'None are missing!'
    """

    nums_set = set(nums)
    range_set = set(range(1, max_num + 1))


    result = list(range_set - nums_set)
    if result == []:
        return "None are missing!"
    return result[0]



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
