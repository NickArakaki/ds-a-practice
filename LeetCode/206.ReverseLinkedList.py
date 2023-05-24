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

# Iterative Solution
def revserSelis(head):
    if head is None: # edge case if empty list
        return

    # build a stack of nodes
    node_stack = []
    curr_node = head

    while (curr_node):
        node_stack.append(curr_node)
        curr_node = curr_node.next

    new_head = node_stack.pop()
    prev_node = new_head
    while(len(node_stack)):
        curr_node = node_stack.pop()
        prev_node.next = curr_node
        prev_node = curr_node

    return new_head
