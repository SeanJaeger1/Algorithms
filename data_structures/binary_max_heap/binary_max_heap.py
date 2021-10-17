import math


class BinaryMaxHeap:
    def __init__(self):
        self._heap = [None]
        self._size = 0

    def __repr__(self):
        return str(self._heap[1:])

    def _parent(self, index):
        return math.floor(index / 2)

    def _left_child(self, index):
        return index * 2

    def _right_child(self, index):
        return index * 2 + 1

    def get_size(self):
        return self._size

    def is_empty(self):
        return True if self._size == 0 else False

    def heapify(self, array_to_add):
        for element in array_to_add:
            self.insert(element)

    def get_max(self):
        return self._heap[1]

    def insert(self, element):
        pass

    def sift_up(self, index):
        sift_index = index
        while (
            sift_index > 0
            and self._heap[self._parent(sift_index)] < self._heap[sift_index]
        ):
            self._heap[self._parent(sift_index)], self._heap[sift_index] = (
                self._heap[sift_index],
                self._heap[self._parent(sift_index)],
            )
            sift_index = self._parent(sift_index)
