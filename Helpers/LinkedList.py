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
