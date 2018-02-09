import unittest

from .binarytree import Node, BinaryTree


class TestNode(unittest.TestCase):

    def test_can_create_node(self):
        n1 = Node(5)
        self.assertEqual(n1.data, 5)
        self.assertIsNone(n1.left)
        self.assertIsNone(n1.right)
        n2 = Node(3)
        self.assertEqual(n2.data, 3)
        self.assertIsNone(n2.left)
        self.assertIsNone(n2.right)

    def test_node_can_attach_to_other_node(self):
        n1 = Node(3)
        n2 = Node(5)
        n3 = Node(4)
        n3.left = n1
        n1.parent = n3
        n3.right = n2
        n2.parent = n3
        self.assertEqual(n3.data, 4)
        self.assertEqual(n3.left.data, 3)
        self.assertEqual(n3.right.data, 5)
        self.assertEqual(n1.parent.data, 4)
        self.assertEqual(n2.parent.data, 4)

    def test_node_can_display_leaf_status(self):
        n1 = Node(5)
        self.assertTrue(n1._is_leaf_node())
        n2 = Node(4)
        n1.left = n2
        self.assertFalse(n1._is_leaf_node())
        self.assertTrue(n2._is_leaf_node())

    def test_node_can_display_left_child_status(self):
        n1 = Node(5)
        n2 = Node(3)
        n1.left, n2.parent = n2, n1
        self.assertTrue(n2._is_left_child())
        n3 = Node(7)
        n1.right, n3.parent = n3, n1
        self.assertFalse(n3._is_left_child())

    def test_node_can_display_root_node_status(self):
        n1 = Node(5)
        self.assertTrue(n1._is_root())


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.b = BinaryTree()

    def test_binary_tree_can_insert_value(self):
        self.b.insert(5)
        r1 = self.b.root.data
        self.assertEqual(r1, 5)
        self.b.insert(15)
        r2 = self.b.root.right.data
        self.assertEqual(r2, 15)
        self.b.insert(0)
        r3 = self.b.root.left.data
        self.assertEqual(r3, 0)

    def test_binary_tree_wont_insert_duplicate(self):
        self.b.insert(10)
        with self.assertRaises(ValueError):
            self.b.insert(10)

    def test_binary_tree_can_search_for_value(self):
        r1 = self.b.search(5)
        self.assertIsNone(r1)
        self.b.root = Node(5)
        r2 = self.b.search(5)
        self.assertIsNotNone(r2)
        self.assertEqual(r2.data, 5)
        r3 = self.b.search(15)
        self.assertIsNone(r3)
        self.b.root.right = Node(15, self.b.root)
        r4 = self.b.search(15)
        self.assertIsNotNone(r4)
        self.assertEqual(r4.data, 15)
        r5 = self.b.search(0)
        self.assertIsNone(r5)
        self.b.root.left = Node(0, self.b.root)
        r6 = self.b.search(0)
        self.assertIsNotNone(r6)
        self.assertEqual(r6.data, 0)

    def test_binary_tree_can_delete_root_leaf_node(self):
        self.b.insert(5)
        self.b.delete(5)
        r1 = self.b.search(5)
        self.assertIsNone(r1)

    def test_binary_tree_can_delete_node_with_one_child(self):
        self.b.insert(15)
        self.b.insert(20)
        self.b.delete(15)
        r1 = self.b.search(15)
        self.assertIsNone(r1)

    def test_binary_tree_can_delete_node_with_two_children(self):
        self.b.insert(20)
        self.b.insert(15)
        self.b.insert(25)
        self.b.delete(20)
        result = self.b.search(20)
        self.assertIsNone(result)
        self.assertEqual(self.b.root.data, 15)
        self.assertEqual(self.b.root.right.data, 25)
