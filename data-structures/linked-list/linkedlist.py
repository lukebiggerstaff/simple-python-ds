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
        if self.head == None:
            self.head = new_node
        else:
            next_node = self.head
            new_node.next = next_node
            self.head = new_node

    def search(self, data):
        node = self.head
        index = 0
        while node != None:
            if node.data == data:
                return index
            index += 1
            node = node.next
        return -1

    def delete(self):
        if self.head == None:
            return 'list is empty'
        self.head = self.head.next

    def list_values(self, node=None):
        if self.head == None:
            return 'list is empty'
        if node == None:
            node = self.head
        print(node.data, end=' ')
        if node.next != None:
            self.list_values(node.next)
