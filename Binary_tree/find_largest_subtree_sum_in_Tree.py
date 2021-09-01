class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right  = None
        
def utility(root,ans):
    if root is None:
        return 0
    ## get the sum  of tree using function
    currsum = (root.data + utility(root.left,ans) + utility(root.right,ans))
    
    ans[0] = max(ans[0],currsum)
    return currsum

def find_largest(root):
    if root is None:
        return 
    
    ans = [-99999999999]
    utility(root,ans)
    return ans
    
## Driver code...@#$!!!!...
if __name__ == "__main__":
    # 
    #         1 
    #        / \ 
    #      /     \ 
   #     -2     3 
   #     / \     / \ 
    #  4   5 -6  2 
    root = Node(1) 
    root.left = Node(-2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(-6) 
    root.right.right = Node(2) 
    print("largest sum is",find_largest(root))
  