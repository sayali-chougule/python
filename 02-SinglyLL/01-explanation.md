## Approach

To reverse a singly linked list in place,the last node becomes the new head, and each node's `next` pointer points to the previous node instead of the next one

1. Using three pointers 
    1. `prev` to know what the current node should now point to
    2. `next_node` to save the original forward link before overwritting it to losing access to the rest of the list.
    3. `curr.next` to save `next_node`

2. Code
    1. `next_node` becomes `curr.next`
    2. `curr.next` becomes `prev`
    3. `prev` becomes `curr`
    4. `curr` becomes `next_node`