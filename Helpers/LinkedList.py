class SinglyLinkedListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class DoublyLinkedListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class SinglyLinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.length = 1


    def append(self, node):
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1


    def remove(self, node):
        dummy_node = SinglyLinkedListNode()
        dummy_node.next = self.head

        prev_node = dummy_node
        curr_node = self.head
        while curr_node:
            if curr_node == node:
                prev_node.next = curr_node.next
                break

        if curr_node == self.head:
            self.head = curr_node.next
        if curr_node == self.tail:
            self.tail = prev_node



    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next
