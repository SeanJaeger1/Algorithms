class BinarySearchTreeNode:
    def __init__(self, value=None, parent=None, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
        self.parent = parent

    def __repr__(self):
        return "Node value is {0}, left node is: {1}, right node is: {2}".format(
            self.value,
            self.left_node.value if self.left_node is not None else None,
            self.right_node.value if self.right_node is not None else None,
        )
