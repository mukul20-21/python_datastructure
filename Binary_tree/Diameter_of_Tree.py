class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def  height(root,ans):
    if root is None:
        return 0
    
    left_height = height(root.left,ans)
    right_height = height(root.right,ans)
    ## To avoid this error TypeError: '>' not supported between instances of 'int' and 'list'
    ## write ans[0] which treat as integer value in max function.
    ans[0] = max(ans[0] , 1+left_height+right_height)
    
    return 1 + max(left_height,right_height)

def  diameter(root):
    if root is None:
        return 0
    ans = [-9999999999]
    height_of_tree = height(root,ans)
    return ans[0]
   
## Driver Code..!!!!
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(70)
root.left.right = Node(90)

print("diameter of the binary tree is--->>>",diameter(root))