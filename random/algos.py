"""
"""
"""
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Counter('hi there') == Counter('ereht ih')

"""
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

from collections import Counter
def group_anagrams(words):
    counts = Counter([tuple(sorted(s)) for s  in words])
    return filter(lambda x: counts[tuple(sorted(x))], words)

#print group_anagrams(words)

"""
Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
"""
nums = [3, 30, 34, 5, 9]

def largest_number(nums):
    string_nums = [str(x) for x in nums]


"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_linked_lists(a, b):
    dummy = c = ListNode(-1)

    while a and b:
        if a.data < b.data:
            c.next = a
            a = a.next
        else:
            c.next = b
            b = b.next

        c = c.next

    c.next = a if not b else a
    return dummy.next


def merge_sort(linked):
    if not linked:
        return

    if len(linked) == 1:
        return linked[0]

    middle = len(linked) / 2
    a = merge_sort(linked[middle:])
    b = merge_sort(linked[:middle])

    merge_linked_lists(a, b)






"""
Remove all duplicates from a list
[1, 1, 2] --> [1,2]
"""

def remove_duplicates(arr):
    count = 0
    hold = {}

    for i in range(len(arr)):
        if arr[i] not in hold:
            hold[arr[i]] = True
            arr[count] = arr[i]
            count += 1

    del arr[count:]

    return arr

print remove_duplicates([1, 2, 2, 4, 3, 4, 1, 2, 2, 3, 4])



"""
Palindrom linked list
"""

class Deque:
    def __init__(self):
        self.items = []

    def add_right(self, item):
        self.items.append(item)

    def add_left(self, item):
        self.items.insert(0, item)

    def pop_left(self):
        return self.items.pop()

    def pop_right(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        tmp = ListNode(item)
        tmp.next = self.head
        self.head = tmp

def is_palindrom(llist):
    tmp = llist.head
    deque = Deque()
    while tmp:
        deque.add_right(tmp.data)
        tmp = tmp.next

    while len(deque.items) > 2:
        if deque.pop_left() != deque.pop_right():
            return False

    return True


l = LinkedList()
l.add(3)
l.add(4)
l.add(4)
l.add(3)


"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [[1,3],[8,10], [2,6], [15,18]]
return [1,6],[8,10],[15,18]
"""

def merge_overlaps(intervals):
    out = []

    sorted_intervals = sorted(intervals, key = lambda x: x[0])

    for interval in sorted_intervals:
        if out and interval[0] <= out[-1][-1]:
            out[-1][-1] = max(interval[-1], out[-1][-1])
        else:
            out.append(interval)
    return out

#intervals = [[1,3],[8,10], [2,6], [15,18]]
#merge_overlaps(intervals)


"""
Weighted nested list sum:
list = [1,[1,2], [2]]
returns = 1*1 + 1*2 + 2*2 + 2*2
"""


def nested_sum(arr):
    if len(arr) == 0:
        return 0

    res = 0
    stack = []
    for item in arr:
        d = 1
        stack.append((item, d))

    while stack:
        item, d = stack.pop()

        if type(item) is int:
            res += item * d
        else:
            for i in item:
                stack.append((i, d + 1))

    return res

nested_sum([1,[1,2],[2]])


"""
2 stacks as a queue
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def queue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        while not self.inbox.is_empty():
            tmp = self.inbox.pop()
            self.outbox.push(tmp)

        return self.outbox.pop()

q = Queue()
q.queue(3)
q.queue(4)
q.queue(9)



"""
group anagrams
input: ["eat", "tea", "tan", "ate", "nat", "bat"]
response:    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
"""



"""
input: ["eat", "tea","hat", "poop" ,"tab","dog",  "ate", "nat", "bat"]
given list of words only return words that are annagrams and return them in their original order
input: ["eat", "tea" ,"tab",  "ate", "bat"]

"""

from collections import defaultdict
l =  ["eat", "tea","hat", "poop" ,"tab","dog",  "ate", "nat", "bat"]

def group_anagrams(arr):
    hold = defaultdict(list)
    count = 0

    for i, w in enumerate(arr):
        sorted_word = ''.join(sorted(w))
        hold[sorted_word].append(i)

    dups = filter(lambda x: len(x[1]) >1, w.items())


    return hold

w = group_anagrams(l)
w




#group anagrams

list = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Word:
    def __init__(self, string, index):
        self.string = string
        self.index = index

def group_anagrams(arr):




"""
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

def product_of_elem(arr):
    res = []
    stack = []
    for i in range(len(arr)):
        stack.append(arr[i])
        arr.remove(arr[i])
        res.append(reduce(lambda x,y: x * y, arr))
        reinsert = stack.pop()
        arr.insert(i, reinsert)

    return res



"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
"""

def find_in_matrix(matrix, item):
    found = False
    if matrix:
        n = len(matrix)
        m = len(matrix[0])
        a = 0
        b = n - 1

        while a < n and b  >= 0:
            print (a,b)
            if matrix[a][b] == item:
                found = True
                return found
            elif matrix[a][b] < item:
                a += 1
            else:
                b -= 1

        return found

find_in_matrix(x, 5)


"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
"""

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,9]

def insert_intervals(intervals, new_interval):
    start = new_interval[0]
    end = new_interval[1]

    l, r = [], []

    for i in intervals:
        if i[1] < start:
            l.append(i)
        elif i[0] > end:
            r.append(i)
        else:
            start = min(start, i[0])
            end = max(end, i[1])

    return l + [[start, end]] + r

insert_intervals(intervals, new_interval)







"""
data structure that has O(1) time for
add
remove
random
"""
import random

class RandomizedSet(object):

    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False


    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop(); self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]








