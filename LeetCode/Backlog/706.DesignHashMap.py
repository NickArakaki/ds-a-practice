"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.

void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.

int get(int key) returns the value to which the specified key is mapped, or -1
if this map contains no mapping for the key.

void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""
class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self, capacity=8):
        self.my_map = [None]*capacity
        self.num_nodes = 0


    def _resize(self) -> list:
        length = len(self.my_map)
        if self.num_nodes + 1 >= length // 2:
            new_map = [None]*(length * 2)

            for list_node in self.my_map:
                while list_node:
                    new_hash = hash(list_node.key) % len(new_map)
                    prev = new_map[new_hash]
                    if not prev:
                        new_map[new_hash] = list_node
                    else:
                        while prev and prev.next:
                            prev = prev.next
                        prev.next = list_node
                    prev = list_node
                    list_node = list_node.next
                    prev.next = None

            self.my_map = new_map

        return self.my_map


    def put(self, key:int, value:int) -> None:
        self._resize()
        key_hash = hash(key) % len(self.my_map)
        llist = self.my_map[key_hash]
        if llist is None:
            self.my_map[key_hash] = ListNode(key, value)
        else:
            prev = llist
            while llist:
                if llist.key == key:
                    llist.val = value
                    return
                prev = llist
                llist = llist.next
            prev.next = ListNode(key,value)
        self.num_nodes += 1
        return


    def get(self, key: int) -> int:
        key_hash = hash(key) % len(self.my_map)
        head = self.my_map[key_hash]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1


    def remove(self, key: int) -> None:
        key_hash = hash(key) % len(self.my_map)
        head = self.my_map[key_hash]
        dummy_node = ListNode()
        dummy_node.next = head
        prev = dummy_node
        while head:
            if head.key == key:
                prev.next = head.next
                self.num_nodes -= 1
                break
            prev = head
            head = head.next
        self.my_map[key_hash] = dummy_node.next


obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(2) == 2)
print(obj.get(3) == -1)
obj.put(2,1)
print(obj.get(2) == 1)
obj.remove(2)
print(obj.get(2) == -1)
