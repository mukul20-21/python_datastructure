class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def utility(root,h):
    if root is None:
        return True
    if (root.left is None and root.right is None):
        if (check.level  == 0):
            check.level = h
            return True
        return check.level == h ## if this comparsion is true its return true else return false..
    
    return utility(root.left,h+1) and utility(root.right,h+1)

def check(root):
    check.level = 0 ## static variable
    h = 0
    
    return utility(root,h)
    

### Driver code..!!!!
if __name__ == "__main__":
    root = Node(12)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(9)
    root.left.left.left = Node(1)
    root.left.right.left = Node(2)
 
    if(check(root)):
        print ("Leaves are at same level")
    else:
        print ("Leaves are not at same level")