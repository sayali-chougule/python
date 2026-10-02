class SinglyLinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    d = SinglyLinkedListNode(data)
    temp = llist
    
    if position == 0:
        d.next = llist
        return d
    for i in range(position-1):
        temp = temp.next
    d.next = temp.next
    temp.next = d
    return llist