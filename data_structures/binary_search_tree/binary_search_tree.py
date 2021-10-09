from binary_search_tree_node import BinarySearchTreeNode


class BinarySearchTree:
    def __init__(self):
        self.root_node = BinarySearchTreeNode()

    def __repr__(self):
        pass

    def insert(self, value):
        # need a subfunction to get the specific value's parent
        pass

    def delete_tree(self):
        self.root_node = BinarySearchTreeNode()

    def get_min(self):
        minimum = self.root_node.value
        current_node = self.root_node.left_node

        while current_node is not None:
            minimum = current_node.value
            current_node = current_node.left_node

        return minimum

    def get_max(self):
        maximum = self.root_node.value
        current_node = self.root_node.right_node

        while current_node is not None:
            maximum = current_node.value
            current_node = current_node.right_node

        return maximum
