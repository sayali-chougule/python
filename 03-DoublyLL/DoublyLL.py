class Node:
    def __init__(self, value=None):
        self.data = value
        self.prev = None
        self.next = None

class DoublyLL:

    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
    # for creating 1st (new) node in LinkedList
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
    
    # creating a node at end
        t = self.head
        while t.next != None:
            t = t.next
    
    
        