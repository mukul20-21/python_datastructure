# Python program to convert binary tree to doubly linked list
## this set-1 approach to convert BT_to_DLL hence their exist 2 more approach..
"""
The problem here is simpler as we don’t need to create a circular DLL, but a simple DLL. The idea behind its solution is quite simple and straight.

    1. If the left subtree exists, process the left subtree
        1. Recursively convert the left subtree to DLL.
        2. Then find the inorder predecessor of the root in the left subtree (the inorder predecessor is the rightmost node in the left subtree).
        3. Make the inorder predecessor as the previous root and the root as the next in order predecessor.
     2.If the right subtree exists, process the right subtree (Below 3 steps are similar to the left subtree).
        1.Recursively convert the right subtree to DLL.
        2.Then find the inorder successor of the root in the right subtree (in order the successor is the leftmost node in the right subtree).
        3.Make the inorder successor as the next root and the root as the previous inorder successor.
    3.Find the leftmost node and return it (the leftmost node is always the head of a converted DLL).
"""




class Node(object):
	
	"""Binary tree Node class has data, left and right child"""
	def __init__(self, item):
		self.data = item
		self.left = None
		self.right = None

def BTToDLLUtil(root):
	
	"""This is a utility function to convert the binary tree to doubly linked list. Most of the core task
	is done by this function."""
	if root is None:
		return root

	# Convert left subtree and link to root
	if root.left:
		
		# Convert the left subtree
		left = BTToDLLUtil(root.left)

		# Find inorder predecessor, After this loop, left will point to the inorder predecessor of root
		while left.right:
			left = left.right

		# Make root as next of predecessor
		left.right = root
		
		# Make predecessor as previous of root
		root.left = left

	# Convert the right subtree and link to root
	if root.right:
		
		# Convert the right subtree
		right = BTToDLLUtil(root.right)

		# Find inorder successor, After this loop, right will point to the inorder successor of root
		while right.left:
			right = right.left

		# Make root as previous of successor
		right.left = root
		
		# Make successor as next of root
		root.right = right

	return root

def BTToDLL(root):
	if root is None:
		return root

	# Convert to doubly linkedlist using BLLToDLLUtil
	root = BTToDLLUtil(root)
	
	# We need pointer to left most node which is head of the constructed Doubly Linked list
	while root.left:
		root = root.left

	return root

def print_list(head):
	
	"""Function to print the given
	doubly linked list"""
	if head is None:
		return
	while head:
		print(head.data, end = " ")
		head = head.right

# Driver Code
if __name__ == '__main__':
	root = Node(10)
	root.left = Node(12)
	root.right = Node(15)
	root.left.left = Node(25)
	root.left.right = Node(30)
	root.right.left = Node(36)

	head = BTToDLL(root)
	print_list(head)

