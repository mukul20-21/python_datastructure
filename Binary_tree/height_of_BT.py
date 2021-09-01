class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def  height (root):
    if root is None:
        return 0
    else:
        return max(height(root.left),height(root.right)) +1                
        ## here 1 return value if the node consist any node as child hence each node return a value..

## Driver code...!!!!

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(70)
root.left.right = Node(90)

print("height of the binary tree is--->>>",height(root))
