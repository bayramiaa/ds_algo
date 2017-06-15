#       10
#      / \
#     3   15
#    / 
#  1   

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None

	def get_val(self):
		return self.val

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

max_value = float('inf')
min_value = float('-inf')

def is_BST(root, min_value, max_value): 
	if root is None:
		return True
	
	if root.get_val() <= min_value or root.get_val() >= max_value:
		return False

	return is_BST(root.get_left_child(), min_value, root.get_val()) and is_BST(root.get_right_child(), root.get_val(), max_value)


node10 = TreeNode(10)
node3 = TreeNode(3)
node15 = TreeNode(15)
node1 = TreeNode(1)
node6 = TreeNode(6)
node10.set_left_child(node3)
node10.set_right_child(node15)
node3.set_left_child(node1)

is_BST(node10, min_value, max_value)

