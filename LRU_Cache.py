#### LRU cache using double linked list

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:   #O(1)
            n = self.dic[key] #O(1)
            self._remove(n)   #O(1)
            self._add(n)      #O(1)
            return n.val
        return None

    def set(self, key, value):
        if key in self.dic: #O(1)
            self._remove(self.dic[key]) #O(1)
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        ### when I remove a node I must set the previous nodes path equal to the next and th
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        ### as new items come in I will add them to the end of my linked list
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


l = LRUCache(3)
l.set('a', 1)
l.set('b', 2)
l.set('c', 3)
l.dic
l.head.next.key