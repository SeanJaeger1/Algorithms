from node import Node

class LinkedList():
    def __init__(self):
        self._head = None    
    
    # adds to the front of the linked list
    def push(self, value):
        if self._head is None:
            self._head = Node(value)
        else:
            new_node = Node(value, next_node=self._head)
            self._head = new_node

    def __repr__(self):
        if self._head is None:
            return "Empty linked list"

        current = self._head
        output = str(self._head.value)

        while current.next_node:
            output = output + " -> " + current.value
            current = current.next_node

        return output
