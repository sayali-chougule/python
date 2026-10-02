class ListNode:
    def __init__(self,val=0, next=None):
        self.val=val
        self.next=next

class Solution(object):
    def mergeTwoLists(self, l1, l2):

    # l1 = [1,3,5]
    # l2 = [1,4,6]

        dummy = ListNode()
        curr = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
    