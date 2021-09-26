from copy import deepcopy

from linked_list import LinkedList


def current_status(current_list):
    status_list = deepcopy(current_list)
    print("List status:")
    print("current list: {0}".format(status_list))
    print("head node: {0}, tail node: {1}".format(status_list.front(), status_list.back()))
    # print("list length: {0}".format(len(status_list)))
    # print("list is empty: {0}".format(status_list.is_empty()))
    # status_list.reverse()
    # print("reversed list: {0}".format(status_list))
    # print("new head node: {0}, new tail node: {1}".format(status_list.front(), status_list.back()))

# Initialize list
example_list = LinkedList()

# Add starting values
example_list.push_front(1)
example_list.push_front(2)
example_list.push_front(3)
example_list.push_back(4)
example_list.push_back(5)

# Pop two values
example_list.pop_front()

# Verify list methods & data
current_status(example_list)
example_list.remove_value(5)
current_status(example_list)
print(example_list.value_n_from_end(-1))