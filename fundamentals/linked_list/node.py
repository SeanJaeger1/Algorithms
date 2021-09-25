class Node():
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_next_node(self, next_node):
        self._next_node = next_node

    def get_next_node(self):
        return self._next_node