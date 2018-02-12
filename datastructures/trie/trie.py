'''
python implemenatation of a trie
'''


class Node(object):

    def __init__(self):
        self.map = dict()
        self.is_end_char = False

    def __repr__(self):
        return '<trie.Node {} is_end={}'.format(
            [_ for _ in self.map],
            self.is_end_char
        )


class Trie(object):

    def __init__(self):
        self.root = Node()

    def _is_last_fork(self, node, char):
        return len(node.map) > 1 or node.map[char].is_end_char

    def insert(self, word):
        current = self.root
        for char in word:
            if char in current.map:
                current = current.map[char]
            else:
                current.map[char] = Node()
                current = current.map[char]
        current.is_end_char = True

    def search(self, word):
        current = self.root
        for char in word:
            if char in current.map:
                current = current.map[char]
            else:
                return False
        if current.is_end_char is not True:
            return False
        return True

    def delete(self, word):
        current = self.root
        last_fork = current, word[0]
        for char in word:
            if char in current.map:
                if self._is_last_fork(current, char):
                    last_fork = current, char
                current = current.map[char]
            else:
                return None
        if current.is_end_char is not True:
            return None
        else:
            last_fork_node, last_fork_char = last_fork[0], last_fork[1]
            if len(last_fork_node.map[last_fork_char].map) == 0:
                del last_fork_node.map[last_fork_char]
            else:
                last_fork_node.map[last_fork_char].is_end_char = False
