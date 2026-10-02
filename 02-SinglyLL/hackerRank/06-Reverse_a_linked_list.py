def reverse(llist):
    # Write your code here
    prev = None
    curr = llist
    while curr:
        new_node = curr.next
        curr.next = prev
        prev = curr
        curr = new_node
    return prev