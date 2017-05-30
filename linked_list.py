class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        tmp = Node(item)
        tmp.next = self.head
        self.head = tmp

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found and current is not None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = previous.next

        if current is None:
            return
        elif previous is not None:
            previous.next = current.next
        else:
            self.head = current.next

    def size(self):
        tmp = self.head
        count = 0

        while tmp is not None:
            count +=1
            tmp = tmp.next

        return count

    def search(self, item):
        tmp = self.head
        found = False

        while not found and tmp is not None:
            if tmp.data == item:
                found = True
            else:
                tmp = tmp.next
        return found

    def get_kth_from_end(self, k):
        l = self.size()
        tmp = self.head
        if k > l:
            return None

        holder = Node()
        for i in range(l - k + 1):
            holder = tmp
            tmp = tmp.next

        return holder.data

    def has_cycle(self):
        slow = fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False

    def reverse_list(self):
        current = self.head
        next = None
        previous = None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous


    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next




l = LinkedList()
l.add(10)
l.add(4)
l.add(15)
l.add(20) #next
l.add(50)
          # current.next
l.print_list()
print "\n \n"
l.reverse_list()
l.print_list()

# circular linked list shit
# l.head.next.next.next.next.next = l.head.next.next
# l.print_list()
