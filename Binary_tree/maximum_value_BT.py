import math
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def  max_value (root):
    if root == None:
        return -math.inf         ## here math.inf function return the infinity value...!!!!
    else:
        ls = max_value(root.left)
        rs = max_value(root.right)
        return max(root.data,ls,rs)


## Driver code...!!!!

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(70)
root.left.right = Node(90)

print("return maximum values from the binary tree is..::--->>>", max_value(root))
