class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def reverse(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse()
            self._insert_at_bottom(temp)

    def _insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self._insert_at_bottom(item)
            self.push(temp)