from binary_search_tree_node import BinarySearchTreeNode


class BinarySearchTree:
    def __init__(self):
        self.root_node = BinarySearchTreeNode()

    def __repr__(self):
        pass

    def insert(self, value):
        if self.root_node.value is None:
            self.root_node.value = value
            return
        elif self.root_node.value == value:
            return

        current_node = self.root_node
        # you now have a starting node that is not none or equal to insertion value

        inserted = False

        while inserted is False:
            # smaller case
            if current_node.value > value:
                if current_node.left_node is None:
                    current_node.left_node = BinarySearchTreeNode(value)
                    inserted = True
                elif current_node.left_node.value == value:
                    inserted = True

                current_node = current_node.left_node

            # larger case
            else:
                if current_node.right_node is None:
                    current_node.right_node = BinarySearchTreeNode(value)
                    inserted = True
                elif current_node.right_node.value == value:
                    inserted = True

                current_node = current_node.right_node

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

    def get_node_count(self):
        def count_nodes(node):
            if node is None:
                return 0
            else:
                return count_nodes(node.left_node) + 1 + count_nodes(node.right_node)

        return count_nodes(self.root_node)