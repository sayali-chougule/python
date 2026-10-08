class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        tmp = head
        tmp1 = head
        while tmp:
            count += 1
            tmp = tmp.next
        if count == n:
            return head.next
        for i in range(count - n -1):
            tmp1 = tmp1.next
        tmp1.next = tmp1.next.next
        return head