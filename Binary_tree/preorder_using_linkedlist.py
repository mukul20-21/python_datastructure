# Create the simple node which store data...!!!!
class Node:
    def  __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def  preorder_print(root):   ## pass object as a parameter...!!!
    if  not root:
        return
    
    print (root.data)
    preorder_print(root.left)
    preorder_print(root.right)


## Driver code..!!!!
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("output depend on the  Preorder(LNR) traversal --- ", preorder_print(root) )
