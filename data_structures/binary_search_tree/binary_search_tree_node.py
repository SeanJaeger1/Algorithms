class BinarySearchTreeNode:
    def __init__(self, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return "Left node is: {0}, right node is: {1}".format(self.left_node, self.right_node)
