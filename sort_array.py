"""You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty
array, you need to return it."""


#====================initial solution======================================

# def sort_array(source_array):

#     result = []
#     odds = []

#     if source_array == []:
#         return result

#     for item in source_array:
#         if item % 2 != 0:
#             odds.append(item)

#     odds.sort()

#     j = 0

#     for i in range(len(source_array)):

#         if source_array[i] % 2 == 0:
#             continue
#         elif source_array[i] % 2 != 0:
#             source_array[i] = odds[j]
#             j += 1
#     return source_array

#===========================more concise solution==========================

def sort_array(source_array):
    result = []
    odds = sorted([n for n in source_array if n % 2 != 0], reverse=True)

    for num in source_array:
        if num % 2 == 0:
            result.append(num)
        else:
            result.append(odds.pop())
    print result






sort_array([5, 3, 2, 8, 1, 4]) #==> [1, 3, 2, 8, 5, 4]
sort_array([5, 3, 1, 8, 0]) #==>  [1, 3, 5, 8, 0]
sort_array([]) #==> []