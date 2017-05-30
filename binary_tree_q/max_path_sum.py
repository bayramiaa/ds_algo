#
#       3
#      / \
#     2   -1
#    / \
#   5  4
#  / \
# -3  -5




class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



def find_max_util(root):

    #base case
    if root is None:
        return 0

    #store max sum in l and r
    l = find_max_util(root.left)
    r = find_max_util(root.right)

    max_single = max(max(l,r) + root.key, root.key)

    #incase path gores through root of tree
    max_top = max(max_single, l + r + max_single)






root = Node(10)
root.left = Node(2)
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)