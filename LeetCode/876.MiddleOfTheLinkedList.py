"""
Given the head of a singly linked list,
return the middle node of the linked list.

If there are two middle nodes,
return the second middle node.

Constraints:
    The number of nodes in the list is in the range [1, 100].

    1 <= Node.val <= 100
"""

def middleNode(head):
    # fast and slow pointers
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
