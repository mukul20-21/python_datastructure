class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None
        
def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(lh,rh) +1


def isBalanced(root):
    if root is None:
        return True
    
    left = height(root.left)
    right = height(root.right)
    
    if (abs(left - right) <= 1) and isBalanced(root.left) is True and isBalanced( root.right) is True:
        return True
    else:
        return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
 
if isBalanced(root):
    print('Tree is balanced')
else:
    print('Tree is not balanced')