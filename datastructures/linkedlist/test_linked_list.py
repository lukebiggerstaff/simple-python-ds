import unittest
import io
from unittest.mock import patch

from .linkedlist import Node, LinkedList


class TestNode(unittest.TestCase):

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


class TestLinkedList(unittest.TestCase):

    def test_linked_list_can_insert(self):
        l1 = LinkedList()
        self.assertIsNone(l1.head)
        l1.insert(5)
        self.assertEqual(l1.head.data, 5)
        l1.insert(4)
        self.assertEqual(l1.head.data, 4)
        self.assertEqual(l1.head.next.data, 5)

    def test_linked_list_can_search(self):
        l1 = LinkedList()
        self.assertIsNone(l1.head)
        l1.insert(5)
        self.assertEqual(l1.head.data, 5)
        result1 = l1.search(5)
        self.assertEqual(result1, 0)
        result2 = l1.search(4)
        self.assertEqual(result2, -1)

    def test_linked_list_can_delete(self):
        l1 = LinkedList()
        l1.insert(5)
        l1.insert(4)
        self.assertEqual(l1.head.data, 4)
        l1.delete()
        self.assertEqual(l1.head.data, 5)
        l1.delete()
        self.assertIsNone(l1.head)
        result = l1.delete()
        self.assertEqual(result, 'list is empty')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_linked_list_can_list_value(self, mock_stdout):
        l1 = LinkedList()
        empty_list_result = l1.list_values()
        self.assertEqual(empty_list_result, 'list is empty')
        l1.insert(5)
        l1.list_values()
        self.assertEqual(mock_stdout.getvalue(), '5 ')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_linked_list_can_list_multiple_values(self, mock_stdout):
        l1 = LinkedList()
        l1.insert(5)
        l1.insert(4)
        l1.list_values()
        self.assertEqual(mock_stdout.getvalue(), '4 5 ')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_linked_list_can_reverse_itself(self, mock_stdout):
        l1 = LinkedList()
        l1.insert(1)
        l1.insert(2)
        l1.insert(3)
        l1.reverse()
        l1.list_values()
        self.assertEqual(mock_stdout.getvalue(), '1 2 3 ')


if __name__ == '__main__':
    unittest.main()
