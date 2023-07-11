"""
Given a linked list, swap every two adjacent nodes
and return its head. You must solve the problem
without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
"""
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = 0
        self.next = next


    def __repr__(self) -> str:
        return f'value = {self.val}'


def swap_pairs(head):
    dummy_node = ListNode(None)
    prev_node = dummy_node
    curr_node = head

    while curr_node and curr_node.next:
        next_node = curr_node.next
        temp = next_node.next

        # swap and reorder next pointers
        next_node.next = curr_node
        curr_node.next = temp
        prev_node.next = next_node

        # update prev_node and curr_node pointers
        prev_node = curr_node
        curr_node = curr_node.next

    return dummy_node.next
