import sys
import math


class Dictionary:
    def __init__(self):
        self.bucket_count = 7
        self.item_count = 0
        self.max_load = 0.4
        self.table = [[] for bucket in range(self.bucket_count)]
        pass

    def __repr__(self):
        return str(self.table)

    def _resize(self):
        new_table = [[] for bucket in range(self.bucket_count * 2)]
        self.bucket_count = self.bucket_count * 2

        for bucket in self.table:
            for item in bucket:
                new_table[self._hash_to_index(item)].append(item)

        self.table = new_table

    def add(self, key, value):
        new_item = [key, value]
        self.item_count = self.item_count + 1

        if self.item_count > self.bucket_count * self.max_load:
            self._resize()

        self.table[self._hash_to_index(new_item)].append(new_item)

        # account for duplicate items

    def _hash_to_index(self, pair):
        position = math.floor(
            self.bucket_count * abs(hash(pair[0])) / 2 ** (sys.hash_info.width - 1)
        )
        return position

    def exists(self, key):
        pass

    def get(self, key):
        pass

    def remove(self, key):
        pass


k = Dictionary()

print(k)
for i in range(20):
    k.add("item-#{0}".format(i), i ** 2)
print(k)