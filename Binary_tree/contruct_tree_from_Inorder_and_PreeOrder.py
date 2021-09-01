class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def built_tree(inorder,preorder,instart,inend):
    if instart>inend:
        return 
    root = Node(preorder[built_tree.pre_index])
    built_tree.pre_index+=1
    
    mid = search(inorder,instart,inend,root.data)
    root.left = built_tree(inorder,preorder,instart,mid-1)
    root.right = built_tree(inorder,preorder,mid+1,inend)
    
    return root
    
def search(arr,start,end,value):
    for i in range(start,end+1):
        if arr[i] == value:
            return i

def utility(root,res):
    if root is None:
        return
    utility(root.left,res)
    utility(root.right,res)
    res.append(root.data)
    return res


def  Postorder_traverse(root):
    res = []
    utility(root,res)
    return res

## Driver code...!!!!!
if __name__ == "__main__":
    
    inorder = [3, 1, 4, 0, 5, 2]
    preorder = [0, 1, 3, 4, 2, 5]
    
    ## function call to built_tree...!!!!
    # Static variable preIndex
    built_tree.pre_index = 0
    root = built_tree(inorder,preorder,0,len(inorder)-1)
    
    
    ## after building the tree in using preorder traversal we traverse using postorder method...
    print(Postorder_traverse(root))