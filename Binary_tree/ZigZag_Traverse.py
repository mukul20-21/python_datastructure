
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def ZigZag(root):
    res = []
    # Base Case
    if root is None:
        return
    currentLevel = []
    nextLevel = []
 
    ltr = True
    currentLevel.append(root)
 
    # Check if stack is empty
    while len(currentLevel) > 0:
        # pop from stack
        temp = currentLevel.pop(-1)
        # print the data
        res.append(temp.data)
 
        if ltr==True:
            # if ltr is true push left
            # before right
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            # else push right before left
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)
 
        if len(currentLevel) == 0:
            # reverse ltr to push node in
            # opposite order
            ltr = not ltr
            # swapping of stacks
            currentLevel, nextLevel = nextLevel, currentLevel
    return res
    
## Driver code....!!!!

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
print("---->>>",ZigZag(root))