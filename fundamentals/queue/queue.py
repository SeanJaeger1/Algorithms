from node import Node

# Essentially a modified linked list
class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self):
        length = 0
        current_node = self._head

        while current_node:
            length = length + 1
            current_node = current_node.get_next_node()

        return length

    def __repr__(self):
        if self._head is None:
            return "Empty queue"

        current_node = self._head.get_next_node()
        output = str(self._head.get_value())

        while current_node:
            output = output + " <- " + str(current_node.get_value())
            current_node = current_node.get_next_node()

        return output

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        if self._head is None:
            inital_node = Node(value)
            self._head, self._tail = inital_node, inital_node
        else:
            new_node = Node(value)
            self._tail.set_next_node(new_node)
            self._tail = new_node

    def dequeue(self):
        if self._head is None:
            raise Exception("This queue has no front value to pop")
        elif self._head is self._tail:
            pop_value = self._head
            self._head, self._tail = None, None
            return pop_value
        else:
            pop_value = self._head.get_value()
            self._head = self._head.get_next_node()

            return pop_value