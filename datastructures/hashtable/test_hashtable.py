import unittest
from .hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.htable = HashTable()

    def test_hash_table_can_hash_integers(self):
        r1 = self.htable._hash(5)
        r2 = self.htable._hash(4)
        self.assertTrue(r1 < len(self.htable.keys))
        self.assertNotEqual(r1, r2)
        r1 = self.htable._hash(5)
        r2 = self.htable._hash(5)
        self.assertEqual(r1, r2)
        self.assertTrue(r2 < len(self.htable.keys))

    def test_hash_table_can_hash_strings(self):
        r1 = self.htable._hash('cat')
        r2 = self.htable._hash('dog')
        self.assertNotEqual(r1, r2)
        self.assertTrue(r1 < len(self.htable.keys))
        r1 = self.htable._hash('cat')
        r2 = self.htable._hash('cat')
        self.assertEqual(r1, r2)
        self.assertTrue(r2 < len(self.htable.keys))

    def test_hash_table_can_put_and_get_values(self):
        self.htable.put('cat', 'dog')
        r1 = self.htable.get('cat')
        self.assertEqual(r1, 'dog')
        self.htable.put(5, 'cat')
        r2 = self.htable.get(5)
        self.assertEqual(r2, 'cat')

    def test_hash_table_can_change_a_keys_value(self):
        self.htable.put('cat', 'dog')
        self.assertEqual(self.htable.get('cat'), 'dog')
        self.htable.put('cat', 'fish')
        self.assertEqual(self.htable.get('cat'), 'fish')

    def test_hash_table_get_fails_properly(self):
        result = self.htable.get('fake')
        self.assertIsNone(result)

    def test_hash_table_can_delete_values(self):
        self.htable.put('cat', 'dog')
        r1 = self.htable.get('cat')
        self.assertEqual(r1, 'dog')
        self.htable.delete('cat')
        r2 = self.htable.get('cat')
        self.assertIsNone(r2)


if __name__ == '__main__':
    unittest.main()
