import random


from binary_max_heap import BinaryMaxHeap

example_heap = BinaryMaxHeap()

number_of_nodes = 15

to_insert = [i for i in range(number_of_nodes)]
random.shuffle(to_insert)

for value in to_insert:
    example_heap.insert(value)

print(example_heap)

for value in to_insert:
    example_heap.extract_max()

print(example_heap)
