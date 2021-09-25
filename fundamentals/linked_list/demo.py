from linked_list import LinkedList


def current_status(current_list):
    print("current list: {0}".format(current_list))
    print("head node is: {0}, tail node is: {1}".format(current_list.front(), current_list.back()))
    print("list length is: {0}".format(len(current_list)))
    print("list is empty: {0}".format(current_list.is_empty()))
    current_list.reverse()
    print("reversed list: {0}".format(current_list))
    print("new head node is: {0}, new tail node is: {1}".format(current_list.front(), current_list.back()))

# Initialize list
example_list = LinkedList()

# Add starting values
example_list.push_front(1)
example_list.push_front(2)
example_list.push_front(3)
example_list.push_back(4)
example_list.push_back(5)

# Pop two values
example_list.pop_back()
example_list.pop_front()

# Verify list methods & data
current_status(example_list)
