import unittest
from .linkedlist import Node


class TestLinkedList(unittest.TestCase):

    def test_node_returns_next_as_none(self):
        n1 = Node(5)
        n2 = Node(4)
        self.assertEqual(n1.next, None)
        self.assertEqual(n2.next, None)

    def test_node_can_store_data(self):
        n1 = Node(5)
        n2 = Node(2)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 2)

    def test_node_can_return_next_node(self):
        n1 = Node(5)
        n1.next = Node(4)
        self.assertIsNotNone(n1.next)
        self.assertTrue(type(n1.next), type(Node))
        self.assertTrue(n1.next.data, 4)

    def test_linked_list_can_insert(self):
        pass


if __name__ == '__main__':
    unittest.main()
