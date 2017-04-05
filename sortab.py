"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    result = []

    if a == []:
        return b
    if b == []:
        return a

    i_a = 0
    i_b = 0

    while i_a < len(a) and i_b < len(b):
        if a[i_a] < b[i_b]:
            result.append(a[i_a])
            i_a += 1
        else:
            result.append(b[i_b])
            i_b += 1

    result.extend(a[i_a:])
    result.extend(b[i_b:])

    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
