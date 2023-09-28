"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise r
eturn -1.

void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Constraints:

1 <= capacity <= 3000

0 <= key <= 104

0 <= value <= 105

At most 2 * 105 calls will be made to get and put.

"""
from collections import deque
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f"key = {self.key}, val = {self.val}"


class Double_Linked_List:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.length = 0


    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        self.length -= 1


    def push(self, node):
        prev = self.tail.prev
        next = self.tail

        node.next = next
        node.prev = prev

        next.prev = node
        prev.next = node

        self.length += 1

        return node


    def print_nodes(self):
        curr_node = self.head
        while curr_node:
            print(curr_node)
            curr_node = curr_node.next



class LRUCache:
    def __init__(self, capacity: int):
        self.list = Double_Linked_List()
        self.cache = {}
        self.capacity = capacity


    def get(self, key:int) -> int:
        # if key in cache
        if key in self.cache:
            node = self.cache[key]

            # move node to end of list
            self.list.remove(node)
            self.list.push(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.list.remove(node)
            self.list.push(node)
            node.val = value
        else:
            if self.list.length == self.capacity:
                head_node = self.list.head.next
                self.list.remove(head_node)
                del self.cache[head_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.list.push(new_node)


cache = LRUCache(2)
cache.put(1,1)
cache.put(1,4)
cache.put(2,2)
print(cache.cache) # dict of node obj
print(cache.get(1)) # 1
cache.put(3,3) # should remove 2
print(cache.cache) # dict of node obj
print(cache.get(2)) # -1
