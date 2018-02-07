'''
Simple representation of a hashtable with collision resolution
performed via chaining
'''


class HashTable(object):

    def __init__(self):
        self.keys = [[] for _ in range(256)]
        self.values = [[] for _ in range(256)]

    def _hash(self, key):
        return hash(key) % len(self.keys)

    def put(self, key, value):
        hashed_key = self._hash(key)
        range_of_chain = range(len(self.keys[hashed_key]))
        is_put = False
        for i in range_of_chain:
            if self.keys[hashed_key][i] == key:
                self.keys[hashed_key][i] = key
                self.values[hashed_key][i] = value
                is_put = True
        if is_put is not True:
            self.keys[hashed_key].append(key)
            self.values[hashed_key].append(value)

    def get(self, key):
        hashed_key = self._hash(key)
        range_of_chain = range(len(self.keys[hashed_key]))
        for i in range_of_chain:
            if self.keys[hashed_key][i] == key:
                return self.values[hashed_key][i]
        return None

    def delete(self, key):
        hashed_key = self._hash(key)
        range_of_chain = range(len(self.keys[hashed_key]))
        for i in range_of_chain:
            if self.keys[hashed_key][i] == key:
                del self.keys[hashed_key][i]
                del self.values[hashed_key][i]
