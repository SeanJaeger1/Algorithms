import math

from binary_search_tree_node import BinarySearchTreeNode


class BinarySearchTree:
    def __init__(self):
        self.root_node = BinarySearchTreeNode()

    def __repr__(self):
        return str(self.print_values())

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
                    current_node.left_node = BinarySearchTreeNode(value, current_node)
                    inserted = True
                elif current_node.left_node.value == value:
                    inserted = True

                current_node = current_node.left_node

            # larger case
            else:
                if current_node.right_node is None:
                    current_node.right_node = BinarySearchTreeNode(value, current_node)
                    inserted = True
                elif current_node.right_node.value == value:
                    inserted = True

                current_node = current_node.right_node

    def is_in_tree(self, value):
        return True if self.get_node(value) is not None else False

    def get_node(self, value):
        if self.root_node.value is None:
            return None
        elif self.root_node.value == value:
            return self.root_node

        current_node = self.root_node
        # you now have a starting node to iterate over searching

        while current_node is not None:
            # smaller case
            if current_node.value > value:
                if current_node.left_node is None:
                    return None
                elif current_node.left_node.value == value:
                    return current_node

                current_node = current_node.left_node

            # larger case
            elif current_node.value < value:
                if current_node.right_node is None:
                    return None
                elif current_node.right_node.value == value:
                    return current_node

                current_node = current_node.right_node

    def delete_tree(self):
        self.root_node = BinarySearchTreeNode()

    def get_min(self, tree_head=None):
        if tree_head is None:
            tree_head = self.root_node

        minimum = tree_head.value
        current_node = tree_head.left_node

        while current_node is not None:
            minimum = current_node.value
            current_node = current_node.left_node

        return minimum

    def get_max(self, tree_head=None):
        if tree_head is None:
            tree_head = self.root_node

        maximum = tree_head.value
        current_node = tree_head.right_node

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

    def get_height(self):
        # This will count the maximum number of edges between any leaf node and the root node

        def get_node_height(node):
            # handle leaf node cases
            if node is None:
                return 0
            elif node.left_node is None and node.right_node is None:
                return 0
            else:
                return (
                    max(
                        get_node_height(node.left_node),
                        get_node_height(node.right_node),
                    )
                    + 1
                )

        return get_node_height(self.root_node)

    def print_values(self):
        def print_tree(node):
            if node is None:
                return []
            elif node.left_node is None:
                return [node.value] + print_tree(node.right_node)
            else:
                return (
                    print_tree(node.left_node)
                    + [node.value]
                    + print_tree(node.right_node)
                )

        return print_tree(self.root_node)

    def _is_BST_util(self, node, minimum_value=-math.inf, maximum_value=math.inf):
        if node is None:
            return True

        return (
            minimum_value < node.value < maximum_value
            and self._is_BST_util(node.left_node, minimum_value, node.value)
            and self._is_BST_util(node.right_node, node.value, maximum_value)
        )

    def is_binary_search_tree(self):
        return self._is_BST_util(self.root_node)

    # def delete_value(self, value):
    #     target_node = self.get_node(value)

    #     if target_node is self.root_node:
    #         self.root_node.value = None

    #     target_node_parent = target_node.parent

    #     if target_node.left_node is None and target_node.right_node is None:
    #         # Node is a leaf, can be safely deleted
    #         if value > target_node_parent.value:
    #             target_node_parent.right_node = None
    #         else:
    #             target_node_parent.left_node = None
    #     elif target_node.left_node is not None and target_node.right_node is not None:
    #         # has both children case
    #         pass
    #     else:
    #         is_smaller = value < target_node_parent.value
