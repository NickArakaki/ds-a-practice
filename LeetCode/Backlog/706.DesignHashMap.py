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
        # check current size of map list
        # if len(map) + 1 >= len(map) // 2
            # new list of len(map) * 2
            # traverse original map
                # rehash each node and add to new list
        # assign self.my_map to new map
        # return self.my_map
        pass


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
