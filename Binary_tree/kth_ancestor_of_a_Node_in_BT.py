class Node:
	def __init__(self,data):
		self.data = data
		self.left = self.right = None
		
def RootToNode(root, key, v): 
   
	if root == None: 
		return False 
  
    # Add current node to the path 
	v.append(root.data) 
  
    # If current node is the target node 
	if root.data == key: 
		return True 
  
    # If the target node exists in the left or the right sub-tree 
	if (RootToNode(root.left, key, v) or RootToNode(root.right, key, v)):
		return True 
  
    # Remove the last inserted node as it is not a part of the path from root to target 
	v.pop() 
	return False 



def kthAncestor(root,k,node):
    #code here
	v = [] 
	RootToNode(root, node, v)
	if k > len(v) - 1 or k <= 0: 
		return -1 
	else:
		return (v[len(v) - 1 - k]) 


## Driver Code...!!!!
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	k = 2
	node = 4
	print(kthAncestor(root,k,node))