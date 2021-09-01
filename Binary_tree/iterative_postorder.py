##using two stacks...

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def iter_postorder(root):
    if root is None:
        return 
   
    s1 = []
    s2 = []
    s1.append(root)
    
    while len(s1)>0:
        item = s1.pop()
        s2.append(item)
        
        if item.left != None:
            s1.append(item.left)
        if item.right != None:
            s1.append(item.right)
    
    while len(s2)>0:
        temp = s2.pop()
        print(temp.data, end = " ")
        
        
### Driver code..!!!!
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    ## function call....
    iter_postorder(root)