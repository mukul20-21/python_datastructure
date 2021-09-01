class Node: 
      
    def __init__(self, data): 
        self.left = None
        self.right = None
        self.data = data 

def toSumTree(Node) :
      
    if(Node == None) :
        return 0
  
    old_val = Node.data 
    Node.data = toSumTree(Node.left) + toSumTree(Node.right) 

    return Node.data + old_val 
  
def printInorder(Node) :
    if (Node == None) :
        return
    printInorder(Node.left) 
    print(Node.data, end = " ") 
    printInorder(Node.right) 
 
# Driver Code 
if __name__ == "__main__": 
  
    root = Node(10) 
    root.left = Node(-2) 
    root.right = Node(6) 
    root.left.left = Node(8) 
    root.left.right = Node(-4) 
    root.right.left = Node(7) 
    root.right.right = Node(5) 
    
    print("Inorder traversa; before convert into Sum tree--->>",printInorder(root))
    
    toSumTree(root) 
     
    print("Inorder Traversal of the resultant tree is--->>> ", printInorder(root) ) 
 