"""
Linked List representation in Python
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            new_node.next = next_node
            self.head = new_node

    def search(self, data):
        node = self.head
        index = 0
        while node is not None:
            if node.data == data:
                return index
            index += 1
            node = node.next
        return -1

    def delete(self):
        if self.head is None:
            return 'list is empty'
        self.head = self.head.next

    def reverse(self, node=None):
        if node is None:
            node = self.head
        if node.next is not None:
            next_node = self.reverse(node.next)
            next_node.next = node
        else:
            self.head.next = None
            self.head = node
        return node

    def list_values(self, node=None):
        if self.head is None:
            return 'list is empty'
        if node is None:
            node = self.head
        print(node.data, end=' ')
        if node.next is not None:
            self.list_values(node.next)
