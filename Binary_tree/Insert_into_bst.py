## insert in bst with both recursive and iterative method...!!!

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def  insert(root,key):
    if root == None:                    ## first boundary case...!!!!
        return Node(key)
    elif root.data == key:
        return root
    elif key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert (root.right,key)
    return root


## driver code...!!!!

root = Node(10)
##root = insert(root,10)
root  = insert(root,20)
root = insert(root,5)
print("properly insert values in bst...")
print(root.left.data)
print(root.right.data)
