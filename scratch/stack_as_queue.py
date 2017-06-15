
class StacksAsQueue:
	def __init__(self):
		self.ins = []
		self.out = []

	def enqueue(self, item):
		self.ins.append(item)

	def dequeue(self):
		if not self.out:
			while self.ins:
				item = self.ins.pop()
				self.out.append(item)
		return self.out.pop()

	def peek(self):
		if not self.out:
			while self.ins:
				item = self.ins.pop()
				self.out.append(item)
		return self.out[-1]




q = StacksAsQueue()
for i in range(3):
	q.enqueue(i)

q.ins == [0, 1, 2]
q.dequeue() == 0
q.enqueue(3)
q.ins == [3]
q.out == [2, 1]