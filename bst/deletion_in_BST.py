## while writing this code alway use higher successor to deleting node...
# cover all corner cases while writing recursive solution..
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        if key < root.data:
            root.left =  insert(root.left,key)
        else:
            root.right =  insert(root.right,key)
    return root
    
def utility(root,res):
    if root is None:
        return
    
    utility(root.left,res)
    res.append(root.data)
    utility(root.right,res)


def inorder(root):
    res = []
    utility(root,res)
    return res

# function to get jst higher order successor... 
def get_high_succ(curr,key):
    while curr.left != None:
        curr = curr.left
    
    return curr.data

## above function are utility function for implementation of delete function..
def del_node(root,key):
    if root is None:
        return 
    if key < root.data:
        root.left = del_node(root.left,key)
    elif key>root.data:
        root.right = del_node(root.right,key)
    
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        else:
            succ = get_high_succ(root.right,key)
            root.data = succ
            root.right = del_node(root.right,succ)
    
    return root
        
        
    
## Driver code...
if __name__ == "__main__":
    root = Node(50)
    
    root = insert(root,30)
    root = insert(root,20)
    root = insert(root,40)
    root = insert(root,70)
    root = insert(root,60)
    root = insert(root,80)
    
    print("Before deletion of node.. ",inorder(root))
    
    del_node(root,70)
    
    print("After deletion of node.. ",inorder(root))
    
    del_node(root,60)
    
    print("After deletion of node.. ",inorder(root))
    
    del_node(root,50)
   
    print("After deletion of node.. ",inorder(root))
    
    
