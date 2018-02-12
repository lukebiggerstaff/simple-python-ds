import unittest

from .suffixtrie import SuffixTrie


class TestSuffixTrie(unittest.TestCase):

    def setUp(self):
        self.s = SuffixTrie()

    def test_suffix_trie_can_insert(self):
        self.s.insert('cat')
        self.assertTrue('c' in self.s.root.map)
        self.assertTrue('a' in self.s.root.map)
        self.assertTrue('t' in self.s.root.map)
        self.assertTrue('a' in self.s.root.map['c'].map)
        self.assertTrue('t' in self.s.root.map['a'].map)
        self.assertTrue('t' in self.s.root.map['c'].map['a'].map)

    def test_suffix_trie_can_search(self):
        self.s.insert('cat')
        r1 = self.s.search('cat')
        self.assertTrue(r1)
        r2 = self.s.search('dog')
        self.assertFalse(r2)

    def test_suffix_trie_can_delete(self):
        self.s.insert('cat')
        r1 = self.s.search('cat')
        self.assertTrue(r1)
        self.s.delete('cat')
        r2 = self.s.search('cat')
        self.assertFalse(r2)
        self.assertTrue('c' not in self.s.root.map)
