"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Recursive Solution
# def reverseList(head):
#     prev = None

#     def _helper(prev, head):
#         if head is None:
#             return prev

#         next_node = head.next
#         head.next = prev
#         return _helper(head, next_node)

#     return _helper(prev, head)
