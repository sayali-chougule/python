class Node:
    def __init__(self, value=None):
        self.data = value
        self.prev = None
        self.next = None

class DoublyLL:

    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value)
