class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def  treesize(root):            ## pass object of above class as parameter of the function..!!!!
    if root == None:
        return 0
    else:
        ls = treesize(root.left)
        rs = treesize(root.right)
        return ls + rs + 1

## driver code------->>>>

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

print("No. of nodes present in the binary tree::-->>>>" , treesize(root)  )