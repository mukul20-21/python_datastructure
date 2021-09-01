class newNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
#path = []        
def utility(root,path,k):
    #global path
    if root is None:
        return 
    path.append(root.data)
    utility(root.left,path,k)
    utility(root.right,path,k)
    
    f = 0
    
    for i in range((len(path)-1),-1,-1):
        f+=path[i]
        if f == k:
            for j in range(i,len(path)):
                print(path[j], end = " ")
            print()
    path.pop()
    

def printKPath(root,k):
    if root is None:
        return
    #global path
    path = [] 
    utility(root,path,k)
    
## Driver Code...!!!!
if __name__ == '__main__':
  
    root = newNode(1) 
    root.left = newNode(3) 
    root.left.left = newNode(2) 
    root.left.right = newNode(1) 
    root.left.right.left = newNode(1) 
    root.right = newNode(-1) 
    root.right.left = newNode(4) 
    root.right.left.left = newNode(1) 
    root.right.left.right = newNode(2) 
    root.right.right = newNode(5) 
    root.right.right.right = newNode(2) 
  
    k = 5
    printKPath(root, k)
    
    #       1
     #   /     \
     #3        -1
    #/   \     /   \
 #2     1   4     5                        
   #     /   / \     \                    
    #  1  1   2     6   
    
'''
##Approach--
    1.Do preorder traverse and store every node in list.
    2.Once we came at last node,start from last node data and store in one variable.
    3.Once the (variable == k), from the index of variable print list at the end.
    4.Then remove last add node(specifically leaf node at start)
    5.Recursively do the same process again & again.