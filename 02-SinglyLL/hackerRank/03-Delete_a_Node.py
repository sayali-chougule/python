def deleteNode(llist, position):
    # Write your code here
    if position == 0:
        return llist.next
    temp = llist
    for i in range(position-1):
        temp = temp.next
    temp.next = temp.next.next
    return llist