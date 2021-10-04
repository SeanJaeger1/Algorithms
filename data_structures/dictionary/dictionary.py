import sys
import math


class Dictionary:
    def __init__(self):
        self.bucket_count = 7
        self.item_count = 0
        self.max_load = 0.4
        self.table = [[] for bucket in range(self.bucket_count)]

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

        for item in self.table[self._hash_to_index(new_item)]:
            if item[0] == key:
                item[1] = value
                return

        self.table[self._hash_to_index(new_item)].append(new_item)

    def _hash_to_index(self, pair):
        position = math.floor(
            self.bucket_count * abs(hash(pair[0])) / 2 ** (sys.hash_info.width - 1)
        )
        return position

    def exists(self, key):
        pass

    def get(self, key):
        for item in self.table[self._hash_to_index([key])]:
            if item[0] == key:
                return item[1]
        
        return None

    def remove(self, key):
        pass


k = Dictionary()

print(k)
for i in range(25):
    k.add("item-#{0}".format(i), i ** 2)
print(k)
k.add("item-#19", 5000)
print(k)
