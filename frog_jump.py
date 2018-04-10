# Determine number of jumps frog must make to get out of the list:

# Example:
# array = [1, 2, 1, 5];
# jumps = 3  (1 -> 2 -> 5 -> <jump out>)

# Return -1 if Frog can't jump out of the array

def solution(a):

    if len(a) == 0:
        return -1

    i = 0
    seen = set()


    while i not in seen:
        seen.add(i)
        i += a[i]
        if not 0 <= i < len(a):
            return len(seen)
    return -1




solution([1, 2, 2, -1]) #4
# solution([1, 2, 1, 5]) #3
# solution([1, -1]) #-1

