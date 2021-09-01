class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        if key < root.data:
            root.left =  insert(root.left,key)
        else:
            root.right =  insert(root.right,key)
    return root
    
def utility(root,res):
    if root is None:
        return
    
    utility(root.left,res)
    res.append(root.data)
    utility(root.right,res)


def inorder(root):
    res = []
    utility(root,res)
    return res
        
## Driver code..!!!

if __name__ == "__main__":
    
    root = Node(50)
    root = insert(root,30)
    root = insert(root,20)
    root = insert(root,40)
    root = insert(root,70)
    root = insert(root,60)
    root = insert(root,80)
    
    print("after Insertion Preorder traversal of BST.. ",inorder(root))
    
    