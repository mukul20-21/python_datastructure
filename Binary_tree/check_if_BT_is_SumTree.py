class node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
## function to get the sum of left and right subtree at every call..
# this function is used as utility function..!!!
def summ(root):
    if(root == None):
        return 0
    return (summ(root.left) + root.data + summ(root.right))
    
## main function to check wether the given tree consist the property of sum tree..
def isSumTree(root):
    if(root == None or (root.left == None and root.right == None)):
            return 1
        
    ls = summ(root.left)
    rs = summ(root.right)
     # check property of sum tree if followed jst return 1 else return 0   
    if((root.data == ls + rs) and isSumTree(root.left) and isSumTree(root.right)):
        return 1
    return 0
    
if __name__ == '__main__':
   
    root = node(26)
    root.left= node(10)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(6)
    root.right.right = node(3)
     
    if(isSumTree(root)):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")