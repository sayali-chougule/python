class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

class Solution(object):
    def reverseList(self, head): 
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev