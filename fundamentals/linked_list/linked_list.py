from node import Node

class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None

    def push_front(self, value):
        if self._head is None:
            inital_node = Node(value)
            self._head, self._tail = inital_node, inital_node
        else:
            new_node = Node(value, next_node=self._head)
            self._head = new_node

    def __repr__(self):
        if self._head is None:
            return "Empty linked list"

        current_node = self._head
        output = str(self._head.value)

        while current_node.next_node:
            output = output + " -> " + current_node.value
            current_node = current_node.next_node

        return output

    def size(self):
        length = 0
        current_node = self._head

        while current_node:
            length = length + 1
            current_node = current_node.next_node

        return length
