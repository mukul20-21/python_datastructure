class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def get_Array(root,res):
    if root is None:
        return
    get_Array(root.left,res)
    res.append(root.data)
    get_Array(root.right,res)
    
def array_to_bst(arr , root):
    if root is None:
        return
     
    array_to_bst(arr, root.left)
 
    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)
 
    # Finally update the right subtree
    array_to_bst(arr, root.right)

def convert(root):
    if root is None:
        return
    
    temp = []
    get_Array(root,temp)
    
    temp.sort()
    
    array_to_bst(temp,root)


def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)


## Driver code..!!!
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.right.right = Node(4)
    ## before convert of binary tree call inorder traversal..
    print("before conversion",inorder(root))
    
    # function call to convert above tree into bst..
    convert(root)
    
    ## after convert print inorder traversal to check our function is work correctly...
    print("after convert",inorder(root))