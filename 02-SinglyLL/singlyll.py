class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMiddle(self, value, x):
        temp = Node(value)
        t1 = self.head 

        while(t1.data != None):
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
        

    def printll(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = SinglyLinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(25)
obj.printll()