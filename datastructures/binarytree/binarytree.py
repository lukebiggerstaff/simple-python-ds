'''
Python representation of binary tree
'''


class Node(object):

    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def _is_leaf_node(self):
        return not self.left and not self.right

    def _has_two_child_nodes(self):
        return self.left is not None and self.right is not None

    def _is_left_child(self):
        return self.parent.left == self

    def _is_right_child(self):
        return self.parent.left == self

    def _is_root(self):
        return self.parent is None

    def _has_left_child(self):
        return self.left is not None

    def _has_right_child(self):
        return self.right is not None

    def __repr__(self):
        return '<class Node data: {} >'.format(self.data)

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def _find_replacement_node(self, node):
        if node.right is None:
            return node
        else:
            return self._find_replacement_node(node.right)

    def insert(self, data, current=None):
        if self.root is None:
            self.root = Node(data)
            return None
        if current is None:
            current = self.root
        if current.data == data:
            raise ValueError('Can not insert duplicate data.')
        if current.data > data:
            if current.left is None:
                current.left = Node(data, parent=current)
            else:
                return self.insert(data, current=current.left)
        if current.data < data:
            if current.right is None:
                current.right = Node(data, parent=current)
            else:
                return self.insert(data, current=current.right)

    def search(self, data, current=None):
        if self.root is None:
            return None
        if current is None:
            current = self.root
        if current.data == data:
            return current
        if current.data > data:
            if current.left is None:
                return None
            else:
                return self.search(data, current=current.left)
        if current.data < data:
            if current.right is None:
                return None
            else:
                return self.search(data, current=current.right)

    def delete(self, data):
        node = self.search(data)
        if node is None:
            return None
        if node._is_leaf_node():
            if node._is_root():
                self.root = None
            else:
                if node._is_left_child():
                    node.parent.left = None
                else:
                    node.parent.right = None
            return None
        if node._has_two_child_nodes():
            replacement = self._find_replacement_node(node.left)
            replacement_data = replacement.data
            self.delete(replacement.data)
            node.data = replacement_data
            return None
        if node._has_left_child():
            node.left.parent = node.parent
            if node._is_root():
                self.root = node.left
            else:
                if node._is_left_child():
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            return None
        if node._has_right_child():
            node.right.parent = node.parent
            if node._is_root():
                self.root = node.right
            else:
                if node._is_left_child():
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            return None

    def __iter__(self):
        if self.root.left:
            yield from self.root.left
        yield self.root
        if self.root.right:
            yield from self.root.right
