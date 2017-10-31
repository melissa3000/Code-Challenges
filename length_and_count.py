"""Linked Lists - Length & Count

Implement Length() to count the number of nodes in a linked list.

length(null) === 0
length(1 -> 2 -> 3 -> null) === 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) === 0
count(1 -> 2 -> 3 -> null, 1) === 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) === 4"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node):
    counter = 0

    if node == None:
        return counter

    while node != None:
        counter += 1
        node = node.next

    print counter


def count(node, data):

    counter = 0

    while node != None:
        if node.data == data:
            counter += 1
        node = node.next
    return counter



# test.assert_equals(count(list, 1), 1, "list should only contain one 1.")
# test.assert_equals(count(list, 2), 1, "list should only contain one 2.")
# test.assert_equals(count(list, 3), 1, "list should only contain one 3.")
# test.assert_equals(count(list, 99), 0, "list should return zero for integer not found in list.")
# test.assert_equals(count(None, 1), 0, "null list should always return count of zero.")

