class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def count(root,low,high):
    if root is None:
        return 0
    ## if low and high both are equal and avoid extra recursive calls...
    if root.data == low and root.data == high:
        return 1
    
    if root.data >= low and root.data <= high:
        return (1 + count(root.left,low,high) + count(root.right,low,high))
    elif root.data < low:
        return count(root.right,low,high)
    else:
        return count(root.left,low,high)
    
 ## Driver code....!!!1
if __name__ == '__main__':
     
    # Let us construct the BST shown in
    # the above figure
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)
     
    # Let us constructed BST shown in above example
    #     10
    #     / \
    #  5     50
    # /       / \
    #1    40 100
    l = 5
    h = 45
    print("Count of nodes between [", l, ", ", h,"] is ", count(root, l, h))