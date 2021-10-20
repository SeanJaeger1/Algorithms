import math


class BinaryMaxHeap:
    def __init__(self):
        self._heap = [None]
        self._size = 0

    def __repr__(self):
        return str(self._heap[1 : self._size])

    def _parent(self, index):
        return math.floor(index / 2)

    def _left_child(self, index):
        return index * 2

    def _right_child(self, index):
        return index * 2 + 1

    def _sift_up(self, index):
        sift_index = index
        while (
            sift_index > 1
            and self._heap[self._parent(sift_index)] < self._heap[sift_index]
        ):
            self._heap[self._parent(sift_index)], self._heap[sift_index] = (
                self._heap[sift_index],
                self._heap[self._parent(sift_index)],
            )
            sift_index = self._parent(sift_index)

    def _sift_down(self, index):
        max_index = index
        l = self._left_child(index)
        r = self._right_child(index)

        if l <= self._size and self._heap[l] > self._heap[max_index]:
            max_index = l
        if r <= self._size and self._heap[r] > self._heap[max_index]:
            max_index = r

        if index != max_index:
            self._heap[index], self._heap[max_index] = (
                self._heap[max_index],
                self._heap[index],
            )
            self._sift_down(max_index)

    def remove(self, index):
        self._heap[index] = math.inf
        self._sift_up(index)
        self.extract_max()

    def change_priority(self, index, new_value):
        old_value = self._heap[index]
        self._heap[index] = new_value
        if new_value > old_value:
            self._sift_up(index)
        else:
            self._sift_down(index)

    def get_size(self):
        return self._size

    def is_empty(self):
        return True if self._size == 0 else False

    def heapify(self, array_to_add):
        for element in array_to_add:
            self.insert(element)

    def get_max(self):
        return self._heap[1]

    def extract_max(self):
        if self._size == 0:
            return None

        result = self._heap[1]
        self._heap[1] = self._heap[self._size]
        self._size = self._size - 1
        self._sift_down(1)
        return result

    def insert(self, element):
        self._size = self._size + 1
        self._heap.append(element)
        self._sift_up(self._size)

    def empty_heap(self):
        self._heap = [None]
        self._size = 0

    def heap_sort(self, array_to_sort):
        self.empty_heap()
        self.heapify(array_to_sort)
        sorted_array = []
        while self._size > 0:
            sorted_array.append(self.extract_max())

        return sorted_array
