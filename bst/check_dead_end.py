class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def utility(root,left,right):
   
    if root is None:
        return False
    if left == right:
        return True
    lh = utility(root.left,left,root.data-1) 
    rh = utility(root.right,root.data+1,right)
    return (lh or rh)

   
def isdeadEnd(root):

    left = 1
    right = 999999999
    if utility(root,left,right):
        return 1
    else:
        return 0
        
## Driver code...!!!
if __name__ == "__main__":
    root = Node(8)
    root.left = Node(5)
    root.right = Node(9)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.left.left.left = Node(1)
    
    print(isdeadEnd(root))
    
    