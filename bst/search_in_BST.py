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
        if  key<root.data:
            root.left =  insert(root.left,key)
        else:
            root.right =  insert(root.right,key)
    return root
    
def search(root,key):
    if root is None:
        return root
    if root.data == key:
        return root
    if  key<root.data:
        return search(root.left,key)
    else:
        return search(root.right,key)
    #return False
        
## Driver code..!!!

if __name__ == "__main__":
    root = Node(50)
    
    root = insert(root,30)
    root = insert(root,20)
    root = insert(root,40)
    root = insert(root,70)
    root = insert(root,60)
    root = insert(root,80)
    
    #print("after Insertion Preorder traversal of BST.. ",preorder(root))
    #search(root,90)
    key = int(input())
    if search(root,key):
        print("Key is present")
    else:
        print("Not found..!!!")
    