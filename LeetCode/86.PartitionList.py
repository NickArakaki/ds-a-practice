"""
Given the head of a linked list and a value x, partition it such
that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""
from Helpers import LinkedList

def partition(head, x: int):
    before_head, after_head = LinkedList.SinglyLinkedListNode(), LinkedList.SinglyLinkedListNode()
    before_curr, after_curr = before_head, after_head

    while head:
        if head.val < x:
            before_curr.next = head
            before_curr = before_curr.next
        else:
            after_curr.next = head
            after_curr = after_curr.next

        head = head.next

    after_curr.next = None
    before_curr.next = after_head.next

    return before_head.next
