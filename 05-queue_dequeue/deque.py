class deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if self.isEmpty():
            print("Queue is Empty")

        else:
            return self.items.pop(0)
        
    def insertAtFront(self,value):
        self.items.insert(0,value)

    def deleteAtEnd(self):
        if self.isEmpty():
            print("Queue is Empty")

        else:
            return  self.items.pop()

dq = deque()
dq.insertAtEnd(10)
dq.insertAtFront(5)
dq.insertAtEnd(15)
dq.insertAtFront(25)
dq.insertAtEnd(50)
dq.insertAtEnd(30)
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtFront())        