"""
You are given the heads of two sorted linked lists
list1 and list2.

Merge the two lists in a one sorted list. The list should
 be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].

-100 <= Node.val <= 100

Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy_node = ListNode()
    curr_node = dummy_node
    curr_1 = list1
    curr_2 = list2

    while curr_1 and curr_2:
        if curr_2.val < curr_1.val:
            # add curr_2 to curr_node
            curr_node.next = curr_2
            curr_2 = curr_2.next
            curr_node = curr_node.next
        else:
            # add curr1 node to curr node
            curr_node.next = curr_1
            curr_1 = curr_1.next
            curr_node = curr_node.next

    curr_node.next = curr_1 if curr_1 is not None else curr_2

    return dummy_node.next

# print(mergeTwoLists([1,2,4], [1,3,4])) # [1,1,2,3,4,4]
# print(mergeTwoLists([], [])) # []
# print(mergeTwoLists([], [0])) # [0]
