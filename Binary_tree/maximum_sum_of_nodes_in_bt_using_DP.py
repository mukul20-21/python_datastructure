## this function is calculate the maximum sum of nodes in B.T. such that no two are adjacent..
## we recursively call  the subtree once I include the root and on second time not included the root jst call the recursive 
## call for grandchildren.
## We store the value in table to avoid repeative recursive calls.

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        

def utility(root):
    if root is None:
        return 0
    
    if root in dp:
        return dp[root]
    
    inc = root.data
    if root.left!=None:
        inc += utility(root.left.left)
        inc += utility(root.left.right)
    
    if root.right != None:
        inc +=utility(root.right.left)
        inc += utility(root.right.right)
    
    exc = utility(root.left) + utility(root.right)
    
    dp[root] = max(inc,exc)
    
    return dp[root]

    
## Driver code...!!!
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.left.left = Node(1)
    dp = dict()
    print("maximum adjacent sum is--",utility(root))
    