import unittest

from .trie import Node, Trie


class TestNode(unittest.TestCase):

    def setUp(self):
        self.n = Node()

    def test_trie_node_has_dict(self):
        self.assertTrue(type(self.n.map) == dict)

    def test_trie_node_has_end_char_attr(self):
        self.assertFalse(self.n.is_end_char)

    def test_trie_node_can_link_to_other_nodes(self):
        self.n.map['a'] = Node()
        self.n.map['a'].map['n'] = Node()
        self.n.map['a'].map['n'].is_end_char = True
        self.assertTrue(self.n.map['a'].map['n'].is_end_char)


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.t = Trie()

    def test_trie_can_insert(self):
        self.t.insert('cat')
        self.assertTrue('c' in self.t.root.map)
        self.assertTrue('a' in self.t.root.map['c'].map)
        self.assertTrue('t' in self.t.root.map['c'].map['a'].map)
        self.assertTrue(self.t.root.map['c'].map['a'].map['t'].is_end_char)

    def test_trie_can_search(self):
        self.t.insert('cat')
        r1 = self.t.search('cat')
        self.assertTrue(r1)
        r2 = self.t.search('fake')
        self.assertFalse(r2)

    def test_trie_can_delete(self):
        self.t.insert('cat')
        r1 = self.t.search('cat')
        self.assertTrue(r1)
        self.t.delete('cat')
        r2 = self.t.search('cat')
        self.assertFalse(r2)
        r3 = self.t.search('c')
        self.assertFalse(r3)

    def test_trie_can_delete_subset(self):
        self.t.insert('cat')
        self.t.insert('cats')
        r1 = self.t.search('cat')
        r2 = self.t.search('cats')
        self.assertTrue(r1)
        self.assertTrue(r2)
        self.t.delete('cat')
        r3 = self.t.search('cat')
        r4 = self.t.search('cats')
        self.assertFalse(r3)
        self.assertTrue(r4)

    def test_trie_can_delete_superset(self):
        self.t.insert('cat')
        self.t.insert('cats')
        r1 = self.t.search('cat')
        r2 = self.t.search('cats')
        self.assertTrue(r1)
        self.assertTrue(r2)
        self.t.delete('cats')
        r3 = self.t.search('cat')
        r4 = self.t.search('cats')
        self.assertFalse(r4)
        self.assertTrue(r3)
