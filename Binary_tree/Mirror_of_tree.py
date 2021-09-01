## Simply swap the left and right link of each Node...!!!
## if the node is leaf node then do anything...
#       5
#       / \
#      3   6
#     / \
#   2   4



class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

def Inorder(root):
    if root is None:
        return 
    Inorder(root.left)
    print(root.data,end = " ")
    Inorder(root.right)

def mirror(root):
    #we recursively call the mirror function which swaps the right subtree with the left subtree.
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left
    
## Driver Code..!!!!
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    
    
    print('Inorder traversal before mirroring', Inorder(root))
    print()
    mirror(root)
    print('Inorder traversal after mirroring', Inorder(root))
