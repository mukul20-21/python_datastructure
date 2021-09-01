class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
# helper function for bst check..
def utility(root,mini,maxi):
    if root is None:
        return True
    if root.data < mini or root.data > maxi:
        return False
    return utility(root.left,mini,root.data-1) and utility(root.right,root.data+1,maxi)
    
## main function to check for bst    
def check(root):
    int_min = -9999999999
    int_max = 9999999999
    if utility(root,int_min,int_max):
        print("Tree is BST")
    else:
        print("Not a bst tree")

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return
        if key < root.data:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    return root
    
## Driver code..!!!

if __name__ == "__main__":
    
    '''
    root = Node(50)
    root = insert(root,30)
    root = insert(root,20)
    root = insert(root,40)
    root = insert(root,70)
    root = insert(root,60)
    root = insert(root,80)
    '''
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)
    
    check(root)