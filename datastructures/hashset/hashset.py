'''
Hash Set representation will take ints and strings
'''


class HashSet(object):

    def __init__(self):
        self.values = [[] for _ in range(256)]

    def _hash(self, value):
        return hash(value) % len(self.values)

    def _retrieve(self, value):
        hash_location = self._hash(value)
        for key, item in enumerate(self.values[hash_location]):
            if item == value:
                return key
        return -1

    def add(self, value):
        hash_location = self._hash(value)
        self.values[hash_location].append(value)

    def remove(self, value):
        index = self._retrieve(value)
        if index != -1:
            hash_location = self._hash(value)
            del self.values[hash_location][index]

    def __contains__(self, value):
        index = self._retrieve(value)
        if index == -1:
            return False
        else:
            return True

    def __iter__(self):
        for chain in self.values:
            # check for empty list []
            # which evaluates False
            if chain is not False:
                for value in chain:
                    yield(value)
