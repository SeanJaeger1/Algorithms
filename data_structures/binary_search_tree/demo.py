from binary_search_tree import BinarySearchTree


example_tree = BinarySearchTree()
example_tree.insert(100)
print(example_tree.root_node)
example_tree.insert(5)
print(example_tree.root_node)
example_tree.insert(1000)
example_tree.insert(1000)
example_tree.insert(12000)

print(example_tree.root_node)
print(example_tree.get_max())
