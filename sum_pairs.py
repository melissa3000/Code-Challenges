"""Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum."""


def sum_pairs(ints, s):

    result = []

    for item in ints:
        x = s - item
        if x in ints:
            result = [item, x]
            break

    if result == []:
            return None
    print result





sum_pairs([1, 4, 8, 7, 3, 15], 8) # == [1, 7]
sum_pairs([1, -2, 3, 0, -6, 1], -6) # == [0, -6]
sum_pairs([20, -13, 40], -7) #== None
sum_pairs([1, 2, 3, 4, 1, 0], 2) #== [1, 1]
sum_pairs([10, 5, 2, 3, 7, 5],  10) #== [3, 7],