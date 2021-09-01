
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def leveltraverse(root):
    res = []
    if root is None:
        return
    q = []
    q.append(root)
    
    while len(q)>0:
        node = q.pop(0)
        res.append(node.data)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

    return res
    
## Driver code....!!!!

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
print("Print the above insert graph in Levelorder traversal type---->>>",leveltraverse(root))