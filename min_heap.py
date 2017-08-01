import heapq

class MinHeap:
	def __init__(self, heap_list = []):
		if heap_list:
			heapq.heapify(heap_list)
		self.heap_list = heap_list

	def push(self, item):
		heapq.heappush(self.heap_list, item)

	def pop(self):
		if len(self.heap_list) > 0:
			return heapq.heappop(self.heap_list)
		else:
			return None

	def peek(self):
		return self.heap_list[0]

	def size(self):
		return len(self.heap_list)

	def is_empty(self):
		return self.size == 0