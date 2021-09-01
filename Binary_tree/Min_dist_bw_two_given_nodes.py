class Node:
	def __init__(self,data):
		self.data = data
		self.left = self.right = None
		
def get_path(root,key,path):
	if root is None:
		return False
	path.append(root.data)
	if (root.data == key):
		return True
	if (get_path(root.left,key,path) or get_path(root.right,key,path)):
		return True
	## if we are on wrong path..
	path.pop()
	return False

def lca(root,n1,n2):
	# get path from root to n1..
	path1 = []
	# get path from root to n2..
	path2 = []
	
	if (get_path(root,n1,path1)!= True or get_path(root,n2,path2) != True):
		return -1
	# Compare the paths to get the first different value/point change..!!!
	i = 0
	while(i < len(path1) and i < len(path2)):
		if path1[i] != path2[i]:
			break
		i += 1
	
	dist = (len(path1)+len(path2) - 2*i)
	return dist

## Driver Code...!!!!
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	
	n1 = 2
	n2 = 3
	print(lca(root,n1,n2))