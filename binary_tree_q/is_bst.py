"""
print left view of binary tree

             12
           /     \
         10       30
        /   \
      8     11

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

n12 = Node(12)
n10 =  Node(10)
n30 = Node(30)
n8 = Node(8)
n11 = Node(11)
n14 = Node(14)

n12.left = n10
n12.right = n30
n10.left = n8
n10.right = n14



INT_MAX = 4294967296
INT_MIN = -4294967296

def is_bst(root, max_int, min_int):
    if root is None:
        return True

    print root.val
    print (max_int, min_int)
    if root.val < min_int or root.val > max_int:
        return False

    return (is_bst(root.left, root.val -1, min_int) and is_bst(root.right, max_int, root.val + 1))

is_bst(n12, INT_MAX, INT_MIN)




