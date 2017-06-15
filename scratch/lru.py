class Node:
	def __init__(self, val, key):
		self.val = val
		self.key = key
		self.next = None
		self.prev = None


class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.dic = dict()
		self.head = Node(0, 0)
		self.tail = Node(0, 0)
		self.head.next = self.tail
		self.tail.prev = self.head

	def set(self, val, key):
		if key in self.dic:
			self._remove(key)
		n = Node(val, key)
		self._add(n)
		self.dic[key] = n
		if len(self.dic) > self.capacity:
			n = self.head.next
			self._remove(n)
			del self.dic[n.key]

	def get(self, key):
		if key in self.dic:
			n = self.dic[key]
			self._remove(n)
			self._add(n)
			return n.val
		return None

	def _add(self, node):
		p = self.tail.prev
		p.next = node
		self.tail.prev = node
		node.prev = p
		node.next = self.tail

	def _remove(self, node):
		p = node.prev
		n = node.next
		p.next = n
		n.prev = p

l = LRUCache(3)
l.set(1, '1')
l.set(2, '2')
l.set(3, '3')

