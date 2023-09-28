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
# def revserSelis(head):
#     prev = None

#     curr_node = head
#     while curr_node:
#         next_node = curr_node.next
#         curr_node.next = prev
#         prev = curr_node
#         curr_node = next_node

#     return prev


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


    def __repr__ (self):
        return f'value = {self.val}'


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail

        self.length = 0


    def append(self, node):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = node
        self.length += 1


    def print_list(self):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            print(curr_node)

l_list = LinkedList()
l_list.append(Node(1))
l_list.append(Node(3))
l_list.print_list()
