class BinaryMaxHeapNode:
    def __init__(self, value=None, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return "Node value is {0}, left node is: {1}, right node is: {2}".format(
            self.value, self.left_node, self.right_node
        )
