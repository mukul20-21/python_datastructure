class getNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def utility(root, Sum, Len, maxLen, maxSum):
    if (not root):
         
        # update maximum Length and maximum Sum
        # according to the given conditions
        if (maxLen[0] < Len):
            maxLen[0] = Len
            maxSum[0] = Sum
        elif (maxLen[0]== Len and maxSum[0] < Sum):
            maxSum[0] = Sum
        return
 
    # recur for left subtree
    utility(root.left, Sum + root.data,Len + 1, maxLen, maxSum)
    # recur for right subtree
    utility(root.right, Sum + root.data,Len + 1, maxLen, maxSum)
    
def sumOfLongRootToLeafPath(root):
        #code here
        if (not root):
            return 0
 
        maxSum = [-999999999999]
        maxLen = [0]
        # finding the maximum Sum 'maxSum' for the maximum Length root to leaf path
        utility(root, 0, 0, maxLen, maxSum)
        return maxSum[0]
        
### Driver Code...!!!!!
if __name__ == "__main__":    
    root = getNode(4)                               #     4    
    root.left = getNode(2)                        #     / \    
    root.right = getNode(5)                     #     2 5    
    root.left.left = getNode(7)                #     / \ / \    
    root.left.right = getNode(1)                # 7 1 2 3
    root.right.left = getNode(2)               #     /        
    root.right.right = getNode(3)           #     6        
    root.left.right.left = getNode(6)
 
    print("Sum = ", sumOfLongRootToLeafPath(root))
     
