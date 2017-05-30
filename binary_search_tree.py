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
max depth
def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
"""


"""
    def maxDepth(self, root):
        if root == None:
            return 0
        l,r = 1,1
        if root.left != None:
            l = l+self.maxDepth(root.left)
        if root.right != None:
            r = r+self.maxDepth(root.right)
        if l>r:
            return l
        else:
            return r
"""