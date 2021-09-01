class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
def right_view(root):
        
        # code here
        if root is None:
            return
        q = []
        q.append(root)
        res = []
        while len(q)>0:
            n = len(q)
        
            for i in range(1,n+1):
                temp = q[0]
                q.pop(0)
            
                if (i==n):
                    res.append(temp.data)
       
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
        
        return res
        

## Driver code...!!!!
if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.right = newNode(7)
    root.right.left = newNode(6)
    root.right.right.left = newNode(8)
    print(right_view(root))
    
    
    #   1
      # /     \
    # 2        3
   #/   \     /  \
 # 4     5   6    7
    #              \
      #             8
