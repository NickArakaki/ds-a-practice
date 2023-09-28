"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from Helpers import LinkedList

def removeNthFromEnd(head, n):
    # initialzie a dummy node with next value as head of llist
    dummy_node = LinkedList.SinglyLinkedListNode(None)
    dummy_node.next = head

    prev_node = dummy_node
    curr_node = head
    next_node = head

    # ititialize a pointer to be n nodes away from head
    for _ in range(n):
        next_node = next_node.next

    # iterate while r pointer has a valid node
    while next_node is not None:
        prev_node = curr_node
        curr_node = curr_node.next
        next_node = next_node.next

    # once at the end remove the l pointer (head-pointer)
    prev_node.next = curr_node.next

    # return next node from dummy node
    return dummy_node.next
