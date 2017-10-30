"""Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum."""






# def sum_pairs(ints, s):

#     result = []
#     seen = {}


#     for i in range(len(ints)):
#         if seen.get((s - ints[i]), 0) != 0:
#             result = [s - ints[i], ints[i]]
#         else:
#             seen[ints[i]] = s - ints[i]
#     if result == []:
#         return None

#     print result


#================solved with sets=================================

def sum_pairs(ints, s):
    seen = set()
    for i in ints:
        if s - i in seen:
            return [s - i, i]
        seen.add(i)







sum_pairs([1, 4, 8, 7, 3, 15], 8) # == [1, 7]
sum_pairs([1, -2, 3, 0, -6, 1], -6) # == [0, -6]
sum_pairs([20, -13, 40], -7) #== None
sum_pairs([1, 2, 3, 4, 1, 0], 2) #== [1, 1]

sum_pairs([10, 5, 2, 3, 7, 5],  10) #== [3, 7],
sum_pairs([5, 9, 13, -3], 10) #== [13, -3]
sum_pairs([0, 2, 0], 0) #== [0, 0],






