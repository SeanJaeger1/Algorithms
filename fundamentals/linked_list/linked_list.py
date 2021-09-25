from node import Node


class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        if self._head is None:
            return true
        else:
            return false

    def push_back(self, value):
        if self._head is None:
            inital_node = Node(value)
            self._head, self._tail = inital_node, inital_node
        else:
            new_node = Node(value)
            self._tail.next_node = new_node
            self._tail = new_node

    def pop_front(self):
        if self._head is None:
            raise IndexError("This list is currently empty")
        else:
            pop_value = self._head.value
            if self._head.next_node:
                self._head = self._head.next_node
            else:
                self._head = None
            return pop_value

    def push_front(self, value):
        new_node = Node(value, self._head)
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

    def front(self):
        if self._head is None:
            raise IndexError("This list is currently empty")
        else:
            return self._head.value

    def back(self):
        if self._tail is None:
            raise IndexError("This list is currently empty")
        else:
            return self._tail.value

    def value_at(self, index):
        node_count = 0
        return_value = None
        selected_node = self._head

        while selected_node is not None:
            if node_count == index:
                return_value = selected_node.value
                break

            selected_node = selected_node.next_node
            node_count = node_count + 1

        if return_value:
            return return_value
        else:
            raise IndexError("There is no node at this index")
        
    def reverse(self):
        if len(self) < 2:
            return

        previous_node = None
        current_node = self._head

        while(current_node is not None):
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
            self._head = previous_node

    def __repr__(self):
        if self._head is None:
            return "Empty linked list"

        current_node = self._head.next_node
        output = str(self._head.value)

        while current_node:
            output = output + " -> " + str(current_node.value)
            current_node = current_node.next_node

        return output

    def __len__(self):
        length = 0
        current_node = self._head

        while current_node:
            length = length + 1
            current_node = current_node.next_node

        return length
