class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
 
def findPreSuc(root, key):
 
    # Base Case
    if root is None:
        return
 
    # If key is present at root
    if root.data == key:
 
        # the maximum value in left subtree is predecessor
        if root.left is not None:
            tmp = root.left
            while(tmp.right):
                tmp = tmp.right
            findPreSuc.pre = tmp
 
        # the minimum value in right subtree is successor
        if root.right is not None:
            tmp = root.right
            while(tmp.left):
                tmp = tmp.left
            findPreSuc.suc = tmp
 
        return
 
    # If key is smaller than root's key, go to left subtree
    if root.data > key :
        findPreSuc.suc = root
        findPreSuc(root.left, key)
 
    else: # go to right subtree
        findPreSuc.pre = root
        findPreSuc(root.right, key)


def insert(root,key):
    if root is None:
        return Node(key)
    
    else:   
        if root.data == key:
            return
        if key < root.data:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    
    return root

## Driver code...!!!!!
if __name__ == "__main__":
    root = Node(50)
    root = insert(root,30)
    root = insert(root,20)
    root = insert(root,40)
    root = insert(root,70)
    root = insert(root,60)
    root = insert(root,80)
    
    ## take input from user to check for predessor and successor..
    findPreSuc.pre = None
    findPreSuc.suc = None
    key = int(input())
    findPreSuc(root, key)
 
    if findPreSuc.pre is not None:
        print ("Predecessor is", findPreSuc.pre.data)
    else:
        print ("No Predecessor")
 
    if findPreSuc.suc is not None:
        print ("Successor is", findPreSuc.suc.data)
    else:
        print ("No Successor")
    
    
   