## jst divide boundary traversal into three part left traversal , leaf_node traversal and last reverse_right_node traversal...

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None
    
def left_node(root,res):
    if root is None:
        return
    elif root.left == None and root.right == None:
        return
    else:
        res.append(root.data)
        left_node(root.left,res)

def leaf_node(root,res):
    if root is None:
         return 
    elif root.left == None and root.right == None:
        res.append(root.data)
    else:
        leaf_node(root.left,res)
        leaf_node(root.right,res)

def reverse_right_node(root,res):  
    if root is None:
        return 
    elif root.left == None and root.right == None:
        return
    else:
        reverse_right_node(root.right,res)
        res.append(root.data)
    
    
    
    
    
def combine(root):
    res = []
    left_node(root,res)
    leaf_node(root,res)
    reverse_right_node(root.right,res) ## jst right.right to ingore the node of the tree..
    
    return res
    
## Driver Code...!!!!

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.right = Node(25)

#res = []
print(combine(root))