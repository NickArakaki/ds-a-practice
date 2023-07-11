"""
Given a linked list, swap every two adjacent nodes
and return its head. You must solve the problem
without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
"""

def swap_pairs(head):
    dummy_node = ListNode(None)
    prev_node = dummy_node
    curr_node = head

    while curr_node and curr_node.next:
        pass

    return dummy_node.next
