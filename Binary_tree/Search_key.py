class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def  searchkey(root,key):
    if root is None:
        return False
    elif root.data == key:
        return True
    elif searchkey(root.left,key) == True:
        return True
    else:
        return searchkey(root.right,key)
        
## Driver code...!!!!
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(70)
root.left.right = Node(90)

print('given key' , searchkey(root,70))