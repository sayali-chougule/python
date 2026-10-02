# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode()
        a = dummy
        dummy.next = head
        while head:
            if head.val == val:
                dummy.next = head.next
                head = head.next
            else:
                head = head.next
                dummy = dummy.next
        return a.next

        