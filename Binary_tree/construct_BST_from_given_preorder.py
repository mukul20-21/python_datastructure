class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def getpointer():
    return utility.pointer

def pointer_increase():
    utility.pointer+=1
    
def utility(preorder,key,mini,maxi,size):
    ## base condition..!!
    if mini > maxi :
        return 
    if (getpointer() >= size):
        return 
    if (preorder[getpointer()] < mini or preorder[getpointer()]>maxi):
        return
    root = None
    
    if (key > mini and key < maxi):
        root = Node(key)
        pointer_increase()
        
        root.left = utility(preorder,preorder[getpointer()],mini,key-1,size)
        root.right = utility(preorder,preorder[getpointer()],key+1,maxi,size)
        
    return root
        
        
    
def construct(preorder):
    left = -999999999
    right = 999999999
    
    size = len(preorder)
    utility.pointer = 0
    root = utility(preorder,preorder[0],l,r,size)
    return root
    
def inorder_utility(root,res):
    if root is None:
        return 
    inorder_utility(root.left,res)
    res.append(root.data)
    inorder_utility(root.right,res)

def inorder(root):
    res = []
    inorder_utility(root,res)
    return res
    
## Driver Code..!!!!
if __name__ == "__main__":
    preorder = [40 , 30 , 22, 34, 50,60,62,65]
    res = construct(preorder)
    
    print("inorder traversal after construction..",inorder(res))