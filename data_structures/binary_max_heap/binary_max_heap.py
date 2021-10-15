import math


class BinaryMaxHeap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def __repr__(self):
        return str(self._heap)

    def get_max(self):
        return self._heap[0]

    def _parent(self, index):
        return math.floor(index / 2)

    def _left_child(self, index):
        return index * 2

    def _right_child(self, index):
        return index * 2 + 1

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
            print(sift_index)
