#Find the minimum number of knight moves between two squares on a grid.  






class KnightToPosition:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

        self.dist = {}
        self.ways = {}


    def gen_legal_moves(self, position):

        possible_moves = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = position[0] + move[0]
            new_y = position[1] + move[1]

            if new_x > self.goal[0] or new_x < 1:
                continue
            if new_y > self.goal[1] or new_y < 1:
                continue

            possible_moves.append((new_x, new_y))


    def run(self):
        queue = [self.start]
        self.dist[self.start] = 0
        self.ways[self.start] = 1

        while len(queue):
            cur = queue.pop()
            if cur == self.goal:
                print "reached goal in  %d moves and %d ways" %(self.dist[cur], self.ways[cur])
                return

            moves = self.gen_legal_moves(p)
            for move in moves:
                return






class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, val):
        tmp = Node(val)
        tmp.next = self.head
        self.head = tmp
        self.length += 1

    def remove(self, val):
        cur = self.head
        prev = None
        found = False

        while not found and cur is not None:
            if cur.val == val:
                found = True
            else:
                prev = cur
                cur = cur.next

        if not found:
            return
        if prev is not None:
            prev.next = cur.next
            self.length -= 1
        else:
            self.head = cur.next
            self.length -= 1

    def get_length(self):
        return self.length

    def get_kth(self, k):
        tmp = self.head

        hold = Node()
        for _ in range(self.length - k + 1):
            hold = tmp
            tmp = self.head.next









