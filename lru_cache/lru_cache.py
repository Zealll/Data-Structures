import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = {}
        self.order = DoublyLinkedList()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if not key in self.storage:
            return None
        
        recent_value = self.storage[key]
        del self.storage[key]
        self.storage[key] = recent_value

        return self.storage[key]

        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        node = self.order.add_to_head(value)

        if key in self.storage:
            self.storage[key] = node.value

        elif len(self.storage) >= self.limit:
            for i in self.storage:
                del self.storage[i]
                break

            self.storage[key] = node.value

        else:
            self.storage[key] = node.value


import time
# def subsetA(arr):
#     # Write your code here
#     start = time.time()
#     sort = sorted(arr) 
#     checker = []
#     second = []
   
#     for i in range(len(arr)-1, -1, -1):
#         checker.append(sort[i])
#         sort = sort[ :i]
#         print(sort)
#         if len(checker) > 1 and sum(checker) > sum(sort):
#             break

#     for i in range(len(checker) - 1, -1, -1):
#         second.append(checker[i])
#     end = time.time()
#     print(end - start)
#     return reversed(checker)


def subsetA(arr):
    # Write your code here
    start = time.time()
    sort = sorted(arr) 
    checker = []
    second = []
   
    for i in range(len(arr)-1, -1, -1):
        checker.append(sort[i])
        sort = sort[ :i]
        if len(checker) > 1 and sum(checker) > sum(sort):
            break
    print(checker)
    return reversed(checker)

print(subsetA([2,1,5,3,4]))