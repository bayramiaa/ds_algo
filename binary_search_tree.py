class BinaryTree():
    def __init__(self, root):
        self.root = root

class TreeNode():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def get_key(self):
        return self.key

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_parent(self):
        return self.parent

    def set_parent(self, obj):
        self.parent = obj

    def set_left_child(self, obj):
        obj.set_parent(self)
        self.left = obj

    def set_right_child(self, obj):
        obj.set_parent(self)
        self.right = obj

    def get_connection(self):
        return [self.left, self.right, self.parent]

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None






node3 = TreeNode(3)
node2 = TreeNode(2)
node_1 = TreeNode(-1)
node5 = TreeNode(5)
node4 = TreeNode(4)
node_3 = TreeNode(-3)
node_5 = TreeNode(-5)



""" serialize/ deserialize
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()


[1, 2, 3, 2, 1, 2, 1]
"""


"""
Binary Tree
           1
         /   \
        2     3
         \
          5
"""
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, obj):
        self.left = obj

    def set_right_child(self, obj):
        self.right = obj

class SearchTree:
    def __init__(self, root):
        self.root = root

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n5 = TreeNode(5)

n1.set_left_child(n2)
n1.set_right_child(n3)
n2.set_right_child(n5)



"""
has path sum
return True or false if sum of path from root to leaf is target
"""
def has_path_sum(root, target):
    if root is None:
        return False

    if root.left is None and root.right is None:
        if root.key == target:
            return True

    return has_path_sum(root.right, target - root.key) or has_path_sum(root.left, target - root.key)



"""
Path sum to target
 find path from root to leaf that sums to target
"""
def path_sum(root, target):
    if root is None:
        return []
    if root.left is None and root.right is None:
        if root.key == target:
            return [[root.key]]
        else:
            return []

    a = path_sum(root.left, target - root.key) + path_sum(root.right, target - root.key)
    return [[root.key] + i for i in a]

path_sum(n1, 8)

""" Find all Paths
input = [1, 2, 3, None, 5]
["1->2->5", "1->3"]
"""


def get_paths(tree):
    root = tree.root
    if not root:
        return []

    queue = [(root, "")]
    res = []

    while queue:
        node, path = queue.pop(0)
        if not node.get_left_child() and not node.get_right_child():
            res.append(path + str(node.key))
        if node.get_right_child():
            queue.append((node.get_right_child(), path + str(node.key) + "->"))
        if node.get_left_child():
            queue.append((node.get_left_child(), path + str(node.key) + "-->"))

    return res

get_paths(n1)

""" Find max_depth
input = [1, 2, 3, None, 5]
return 3
"""

def get_max_depth(root):
    if root:
        return 1 + max(map(get_max_depth, (root.get_left_child(), root.get_right_child())))
    else:
        return 0

get_max_depth(n1)



"""
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return not self.left and not self.right


def level_order_traversal(root):
    if root is None:
        return []

    res = []
    level = [root]

    while level:
        current_nodes = []
        next_nodes =[]

        for node in level:
            current_nodes.append(node.val)

            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        level = next_nodes
        res.append(current_nodes)

    return res

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)
n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7

level_order_traversal(n3)

def find_max_depth(root):
    if root is None:
        return 0
    else:
        return 1 + max(find_max_depth(root.left) , find_max_depth(root.right))


def find_all_paths(root):
    if root is None:
        return []

    queue = [(root, "")]
    res = []
    while queue:
        node, path = queue.pop(0)
        if not node.right and not node.left:
            res.append(path + str(node.val))

        if node.right:
            queue.append((node.right, path + str(node.val) + ','))
        if node.left:
            queue.append((node.left, path + str(node.val) + ','))

    return res


def root_to_path_target(root, target):
    if root is None:
        return []
    if root.right is None and root.left is None:
        if root.val == target:
            return [[root.val]]
        else:
            return []

    a = root_to_path_target(root.left, target - root.val) + root_to_path_target(root.right, target - root.val)

    return [[root.val] + i for i in a]

"""
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

serialize binary tree
output : [3, 9, 20, #, #, 15 7]
"""

def tree_to_list(root):

    def run(node):
        if node:
            res.append(node.val)
            run(node.left)
            run(node.right)
        else:
            res.append('#')

    res = []
    run(root)
    print res
    return ''.join(res)


# def serialize(self, root):
#     def doit(node):
#         if node:
#             vals.append(str(node.val))
#             doit(node.left)
#             doit(node.right)
#         else:
#             vals.append('#')
#     vals = []
#     doit(root)
#     return ' '.join(vals)
