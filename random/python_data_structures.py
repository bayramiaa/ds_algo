

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self, item):
        return self.items.pop()

    def size(self):
        return len(self.items)
"""
for Deque data structure
    def add_front(self, item):
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop(0)
"""

class List:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def search(self, item):
        return item in self.items

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def append(self, item):
        self.items.append()

    def index(self, item):
        return self.items.index(item)

    def insert(self, item, index):
        self.items.insert(index, item)

    def pop(self):
        return self.items.pop()

    def pop_pos(self, item, index):
        return self.items.pop(index)


"""
Unordered list 
As we suggested above, the unordered list will be built from a collection of nodes,
 each linked to the next by explicit references.

 "Finding a specific element in a linked list, even if it is sorted, normally requires O(n) time (linear search). This is one of the primary disadvantages "
"""
class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self): ## checking if no nodes in 
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False

        while not found and current != None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    #def pop(self): def index(self, item), 

    def append(self, item):
        current = self.head
        count =0
        while current.get_next() != None:
            current = current.get_next()

        current.set_next(Node(item))


    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


"""
Ordered List
The structure of an ordered list is a collection of items where each 
item holds a relative position that is based upon some underlying characteristic of the item.
 The ordering is typically either ascending or descending and we assume that list items have a 
 meaningful comparison operation that is already defined. Many of the ordered list operations are the same as those of the unordered list.
 """

class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count +=1
            current = current.get_next()

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found and current != None:
            if current.get_data == item:
                found = True
            else:
                previous = current
                current = previous.get_next()

        if previous == None:
            self.head == current.get_next()
        else:
            previous.get_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while not found and current != None and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while not stop and current != None:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = previous.get_next()

        tmp = Node(item)

        if previous == None:
            tmp.set_next(self.head)
            self.head = tmp
        else:
            previous.set_next(tmp)
            tmp.set_next(current)


### Node
class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next







def baseN(item, base):
    char = "0123456789ABCDEF"
    if item < base:
        return char[item]

    q, r = divmod(item, base)

    return baseN(q, base) + char[r]


def reverse(s):
    if len(s) == 1:
        return s

    return reverse(s[1:]) + s[0]



def dedup_sentence(array):






#### Find the Least Common Anncestor 


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = node(3)
root.right.left = Node(6)
root.right.right = Node(7)


class Node():
    def __init__(self, key):
        self.key = key
        self.left = left
        self.right = right

def find_path(root, path, k):

    if root is None:
        return False

    path.append(root)

    if root.key == k:
        return True

    if (root.left is not None and find_path(root.left, path, k)) and
       (root.right is not None and find_path(root.right, path, k)):
       return True

    path.pop()
    return False


def find_LCA(root, k1, k2):







"""
print left view of binary tree

         12
       /     \
     10       30
            /    \
          25      40 

"""

class Node():
    def __init__(self, key):
        self.key = key
        self.left = left 
        self.right = right


root = Node(12)
root.left = Node(10)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(40)

def get_left_level(root):

    if root is None:
        return False

    if root.left is not None









"""
linked list
"""

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def get_length(self):
        count = 0
        tmp = self.head
        while tmp.data is not None:
            tmp = tmp.next
            count += 1

        return count

    def get_kth(self, k):        
        if self.head is None:
            return 

        l = self.get_length()
        tmp = self.head

        for i in range(len(l - k + 1)):
            tmp = tmp.next

        return tmp.data

l = LinkedList()
l.add(Node(1))
l.add(Node(4))
l.add(Node(5))
l.add(Node(10))
l.add(Node(3))

l.get_length()
l.get_kth(3)









