"""
Given the head of a llist remove the nth node from the end
"""
from Helpers import SinglyLinkedListNode

def remove_nth_node(head, n):
    dummy_node = SinglyLinkedListNode()
    dummy_node.next = head

    right_node = head
    while n > 1:
        right_node = right_node.next

    prev_node = dummy_node
    left_node = head
    while right_node.next:
        right_node = right_node.next
        prev_node = prev_node.next
        left_node = left_node.next

    prev_node.next = left_node.next
    return dummy_node.next
