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
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.my_map = []


    def _resize(self) -> list:
        length = len(self.my_map)
        if length + 1 >= length // 2:
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
                    list_node = list_node.next

            self.my_map = new_map

        return self.my_map


    def put(self, key:int, value:int) -> None:
        # call _resize
        # create a new node with key and value
        # hash key % len(input)
        # traverse llist
            # if we find a node with same key, update val
            # else add new node to end of list
        # return
        pass


    def get(self, key: int) -> int:
        # hash key % len(map)
        # key into my_map with hashed key
        # iterate thru llist find node with key
            # if we find node return val
            # else return -1
        pass


    def remove(self, key: int) -> None:
        # hash key % len(map)
        # key into map and traverse llist until we find node with key
            # remove node
        # return
        pass


obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(2) == 2)
print(obj.get(3) == -1)
obj.put(2,1)
print(obj.get(2) == 1)
obj.remove(2)
print(obj.get(2) == -1)
