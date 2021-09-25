from linked_list import LinkedList


example_list = LinkedList()

print(example_list)
example_list.push_front(1)
print(example_list)
example_list.push_back(5)
print(example_list)
example_list.push_front(7)
print(example_list)
example_list.reverse()
print(example_list)
print(example_list.value_at(8))