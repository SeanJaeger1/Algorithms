import sys
import math


class Dictionary:
    def __init__(self):
        self.bucket_count = 7
        self.item_count = 0
        self.max_load = 0.75
        self.table = [[] for bucket in range(self.bucket_count)]

    def __repr__(self):
        return str(self.table)

    def _resize(self):
        self.bucket_count = self.bucket_count * 2
        new_table = [[] for bucket in range(self.bucket_count)]

        for bucket in self.table:
            for item in bucket:
                new_table[self._hash_to_index(item[0])].append(item)

        self.table = new_table

    def add(self, key, value):
        if self.item_count > self.bucket_count * self.max_load:
            self._resize()

        for item in self.table[self._hash_to_index(key)]:
            if item[0] == key:
                item[1] = value
                return

        self.table[self._hash_to_index(key)].append([key, value])
        self.item_count = self.item_count + 1

    def _hash_to_index(self, key):
        position = math.floor(
            self.bucket_count * abs(hash(key)) / 2 ** (sys.hash_info.width - 1)
        )
        return position

    def exists(self, key):
        for item in self.table[self._hash_to_index(key)]:
            if item[0] == key:
                return True

        return False

    def get(self, key):
        for item in self.table[self._hash_to_index(key)]:
            if item[0] == key:
                return item[1]

        return None

    def remove(self, key):
        for index, item in enumerate(self.table[self._hash_to_index(key)]):
            if item[0] == key:
                self.table[self._hash_to_index(key)].pop(index)
                self.item_count = self.item_count - 1
                return
