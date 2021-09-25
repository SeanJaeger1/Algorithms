from linked_list import LinkedList


def current_status(current_list):
    print("current list: {0}".format(current_list))
    print("head node is: {0}, tail node is: {1}".format(current_list._head.get_value(), current_list._tail.get_value()))


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

current_status(example_list)