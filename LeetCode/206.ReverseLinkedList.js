// """
// Given the head of a singly linked list, reverse the list, and return the reversed list.
// """
// # Recursive Solution
// # def reverseList(head):
// #     prev = None

// #     def _helper(prev, head):
// #         if head is None:
// #             return prev

// #         next_node = head.next
// #         head.next = prev
// #         return _helper(head, next_node)

// #     return _helper(prev, head)

// # Iterative Solution
// # def revserSelis(head):
// #     prev = None

// #     curr_node = head
// #     while curr_node:
// #         next_node = curr_node.next
// #         curr_node.next = prev
// #         prev = curr_node
// #         curr_node = next_node

// #     return prev

class Node {}

function reverseList(head) {
  let prev = null;
}
