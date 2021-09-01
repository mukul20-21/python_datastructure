class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
subtree = set()
def  duplicate(root):
    if root is None:
        return "$"
    subtree = set()
    q = []
    q.append(root)
    
    while len(q)>0:
        temp = q[0]
        q.pop(0)
        
        # To store the left and the right children of the current node 
        l = ' '
        r = ' '
        # left subtree
        if temp.left != None:
            l = temp.left.data
            q.append(temp.left)
        # iright subtree
        if temp.right != None:
            r = temp.right.data
            q.append(temp.right)
            
        subt=""
        subt += str(temp.data)
        subt += str(l) 
        subt += str(r) 
        
        if (l != ' ' or r != ' '):
          # If this subtree count is greater than 0 that means duplicate exists 
            subtree.add(subt)
            if (len(subtree) > 1):
                return True
    return False   
        
        
## Driver code..!!!!
if __name__ == "__main__":
	root = Node(1)
    	root.left = Node(2) 
    	root.right = Node(3)
    	root.left.left = Node(4)
    	root.left.right =Node(5)
    	root.right.right = Node(2)
    	root.right.right.left = Node(4)
    	root.right.right.right = Node(5)
    
    	print(duplicate(root))
    