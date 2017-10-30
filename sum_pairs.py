"""Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum."""


# def sum_pairs(ints, s):

#     result = []

#     for item in ints:
#         x = s - item
#         if x in ints:
#             result = [item, x]
#             break

#     if result == []:
#             return None
#     print result



def sum_pairs(ints, s):

    result = []
    pairs = {}

    for item in ints:
        x = s - item
        i = 0
        if pairs.get(ints[i], 0) == 0:
            pairs[item] =



# Can I solve this using a hash table? revisit with this strategy, how to approach?

# look at ints[i] --- if not in dict, add it with val: s - ints[i]
# {1: 7, 4: 4, 8: 0, 7: 1, 3: 5, 15: -7}
#
#check for s - ints[0] in dict,
#if {1:7} in dict, add key, val to result



sum_pairs([1, 4, 8, 7, 3, 15], 8) # == [1, 7]
sum_pairs([1, -2, 3, 0, -6, 1], -6) # == [0, -6]
sum_pairs([20, -13, 40], -7) #== None
sum_pairs([1, 2, 3, 4, 1, 0], 2) #== [1, 1]

sum_pairs([10, 5, 2, 3, 7, 5],  10) #== [3, 7],
sum_pairs([5, 9, 13, -3], 10) #== [13, -3]