# Given root of tree with arbitrary number of children nodes transform data
# from tree to list. Where data from neighbour nodes in tree located in
# neighbour position in list.


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    result = [tree_root.data]
    to_visit = tree_root.child_nodes

    while to_visit:
        target = to_visit.pop(0)
        result.append(target.data)
        if target.child_nodes:
            to_visit += target.child_nodes


    print result




tree_to_list(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])]))
# =>
# [1, 2, 3, 3, 4, 5, 7])