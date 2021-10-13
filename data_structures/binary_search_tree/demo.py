import random

from binary_search_tree import BinarySearchTree


example_tree = BinarySearchTree()

to_insert = [i for i in range(20)]
# random.shuffle(to_insert)

for value in to_insert:
    example_tree.insert(value)

# print(example_tree.get_node_count())
# print(example_tree.get_max())
# print(example_tree.get_min())
# print(example_tree.get_height())
# print(example_tree.is_binary_search_tree())
print(example_tree)
example_tree.delete_value(19)
print(example_tree)
