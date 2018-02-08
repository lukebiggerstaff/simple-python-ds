import unittest
from .hashset import HashSet


class TestHashSet(unittest.TestCase):

    def setUp(self):
        self.h = HashSet()

    def test_hash_set_can_add_values(self):
        self.h.add(4)
        self.assertTrue(4 in self.h)
        self.h.add(500000)
        self.assertTrue(500000 in self.h)

    def test_hash_set_can_remove_values(self):
        self.h.add('dog')
        self.assertTrue('dog' in self.h)
        self.h.remove('dog')
        self.assertTrue('dog' not in self.h)

    def test_hash_set_can_iterate_over_all_values(self):
        self.h.add(1)
        self.h.add(2)
        h_generator = self.h.__iter__()
        self.assertEqual(h_generator.__next__(), 1)
        self.assertEqual(h_generator.__next__(), 2)
        with self.assertRaises(StopIteration):
            h_generator.__next__()
