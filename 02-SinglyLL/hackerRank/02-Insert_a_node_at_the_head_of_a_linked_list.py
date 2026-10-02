class SinglyLinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertNodeAtHead(llist, data):
    # Write your code here]
    
    new_node = SinglyLinkedListNode(data)

    new_node.next = llist

    return new_node