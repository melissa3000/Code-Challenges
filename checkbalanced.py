"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False

Imbalanced Six:

    1
   / \
  2   6
 / \
3   4
   /
  5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False
"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?"""

        def _num_descendants(node):
          """ Returns None if imbalanced"""

          # base case: node is a childe of a leaf (not a node)
          if not node:
            return 0

          left = _num_descendants(node.left)

          if left is None:
            return None

          right = _num_descendants(node.right)

          if right is None:
            return None

          if abs(left - right) > 1:
            return None

          #Height of deepest descendant + self
          return max(left, right) + 1

        return _num_descendants(self) is not None


        # This solution breaks when the tree branches multiple times

        # left_depth = 0
        # right_depth = 0

        # current = self

        # while current.left != None:
        #   left_depth += 1
        #   current = current.left
        # print "l:", current
        # print left_depth

        # current = self
        # while current.right != None:
        #   right_depth += 1
        #   current = current.right
        # print "r: ", current
        # print right_depth

        # if abs(left_depth - right_depth) <= 1:
        #   return True

        # else:
        #   return False




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
