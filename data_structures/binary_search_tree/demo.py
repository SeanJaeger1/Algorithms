import random

from binary_search_tree import BinarySearchTree


example_tree = BinarySearchTree()

number_of_nodes = 100

to_insert = [i for i in range(number_of_nodes)]
random.shuffle(to_insert)

for value in to_insert:
    example_tree.insert(value)

# print(example_tree.get_node_count())
# print(example_tree.get_max())
# print(example_tree.get_min())
# print(example_tree.get_height())
# print(example_tree.is_binary_search_tree())
print(example_tree)
