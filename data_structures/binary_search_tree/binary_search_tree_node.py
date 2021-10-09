class BinarySearchTreeNode:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return "Node value is {0}, left node is: {0}, right node is: {1}".format(
            self.value, self.left_node, self.right_node
        )
