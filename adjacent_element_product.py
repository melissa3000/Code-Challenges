# Task
# Given an array of integers, Find maximum product obtained from multiplying 2 adjacent numbers .

# Notes
# Array will contain at least 2 elements.

# Aarray may contain positive/negative numbers and zeroes.

# Input >> Output Examples
# adjacent_elements_product([1,2,3])  ==>  return 6
# Explanation:
# Max product obtained from multiplying 3 * 2 = 6 .

# adjacent_elements_product([9, 5, 10, 2, 24, -1, -48])  ==>  return 50
# Explanation:
# Max product obtained from multiplying 5 * 10 = 50 .

# adjacent_elements_product([-23, 4, -5, 99, -27, 329, -2, 7, -921])  ==>  return -14


# refactored:
def adjacent_element_product(array):
    return max(array[i] * array[i + 1] for i in range(len(array) - 1))




# brute force:
# def adjacent_element_product(array):
#     current_max = -1000000000

#     for i in range(len(array) - 1):
#         if array[i] * array[i + 1] > current_max:
#             current_max = array[i] * array[i + 1]
#     print current_max

adjacent_element_product([4, 12, 3, 1, 5]) #=> 48)


