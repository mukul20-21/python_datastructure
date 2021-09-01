class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def  itr_preorder(root):
    if root is None:
        return
    
    st = [root]                         # insert initially root in a list...!!!! 
    while len(st)>0:
        curr = st.pop()
        print(curr.data)
        if curr.right is not None:
            st.append(curr.right)
        if curr.left is not None:
            st.append(curr.left)


## Driver code...!!!!

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("here the preorder traversal of binary using iterative method..--->",itr_preorder(root))
