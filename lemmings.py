"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # max_distance = None

    if num_holes == len(cafes):
        return 0

    # distance1 = cafes[0] - 0
    # distance2 = num_holes - cafes[-1] - 1
    # distance3 = (cafes[-1] - cafes[0]) / 2

    # max_distance = max(distance1, distance2, distance3)

    # return max_distance

    max_distance = 0

    for hole in range(num_holes):
        distance = min([abs(hole - cafe) for cafe in cafes])

        max_distance = max(max_distance, distance)
    return max_distance



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
