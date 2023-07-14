from Helpers import LinkedList

node1 = LinkedList.SinglyLinkedListNode(1)
node2 = LinkedList.SinglyLinkedListNode(2)
node3 = LinkedList.SinglyLinkedListNode(3)
node4 = LinkedList.SinglyLinkedListNode(4)
node5 = LinkedList.SinglyLinkedListNode(5)

llist = LinkedList.SinglyLinkedList(node1)
llist.append(node2)
llist.append(node3)
llist.append(node4)
llist.append(node5)
llist.print_list()
