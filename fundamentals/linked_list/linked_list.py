from node import Node


class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def push_back(self, value):
        if self._head is None:
            inital_node = Node(value)
            self._head, self._tail = inital_node, inital_node
        else:
            new_node = Node(value)
            self._tail.set_next_node(new_node)
            self._tail = new_node

    def pop_front(self):
        if self._head is None:
            raise Exception("This list has no front value to remove")
        else:
            pop_value = self._head.get_value()
            if self._head.get_next_node():
                self._head = self._head.get_next_node()
            else:
                self._head = None
            return pop_value

    def pop_back(self):
        if self._head is None or self._tail is None:
            raise Exception("This list has to end value to remove")
        elif self._head is self._tail:
            self._head, self._tail = None, None
        else:
            current_node = self._head

            while current_node.get_next_node() is not self._tail:
                current_node = current_node.get_next_node()

            self._tail = current_node
            self._tail.set_next_node(None)

    def push_front(self, value):
        new_node = Node(value, self._head)
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

    def front(self):
        if self._head is None:
            raise IndexError("This list is currently empty")
        else:
            return self._head.get_value()

    def back(self):
        if self._tail is None:
            raise IndexError("This list is currently empty")
        else:
            return self._tail.get_value()

    def value_at(self, index):
        node_count = 0
        return_value = None
        selected_node = self._head

        while selected_node is not None:
            if node_count == index:
                return_value = selected_node.get_value()
                break

            selected_node = selected_node.get_next_node()
            node_count = node_count + 1

        if return_value:
            return return_value
        else:
            raise IndexError("There is no node at this index")
        
    def insert(self, index, value):
        if index == 0:
            self.push_front(value)
            return

        node_count = 0
        selected_node = self._head

        while selected_node is not None:
            if node_count == index - 1:

                node_to_insert = Node(value, selected_node.get_next_node())
                selected_node.set_next_node(node_to_insert)

                if selected_node == self._tail:
                    self._tail = node_to_insert
                
                return

            selected_node = selected_node.get_next_node()
            node_count = node_count + 1

        raise IndexError("There is no node at this index")

    def reverse(self):
        if len(self) < 2:
            return

        previous_node = None
        current_node = self._head

        self._tail = self._head

        while(current_node is not None):
            next_node = current_node.get_next_node()
            current_node.set_next_node(previous_node)
            previous_node = current_node
            current_node = next_node
            self._head = previous_node

    def __repr__(self):
        if self._head is None:
            return "Empty linked list"

        current_node = self._head.get_next_node()
        output = str(self._head.get_value())

        while current_node:
            output = output + " -> " + str(current_node.get_value())
            current_node = current_node.get_next_node()

        return output

    def __len__(self):
        length = 0
        current_node = self._head

        while current_node:
            length = length + 1
            current_node = current_node.get_next_node()

        return length
