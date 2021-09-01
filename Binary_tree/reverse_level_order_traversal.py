class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def reverse_level_traverse(root):
    q = []
    if root is None:
            return
    q.append(root)
    ans = []
    
    while len(q)>0:
        
        node = q.pop(0)
        ans.insert(0,node.data)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
              
    return ans
    
## Driver code....!!!!

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
print("Reverese Levelorder traversal---->>>",reverse_level_traverse(root))