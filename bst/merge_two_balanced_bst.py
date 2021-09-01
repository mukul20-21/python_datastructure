class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        

def get_array_from_bst(root,res):
    if root is None:
        return
    get_array_from_bst(root.left,res)
    res.append(root.data)
    get_array_from_bst(root.right,res)
    
def convert_array_to_bst(nums):
    if not nums:
        return
    mid = len(nums)//2
    root = Node(nums[mid])
    root.left = convert_array_to_bst(nums[:mid])
    root.right = convert_array_to_bst(nums[mid+1:])
    
    return root

def merge_bst(root1,root2):
    arr1 = []
    
    ## get element from both bst into single array..
    get_array_from_bst(root1,arr1)
    get_array_from_bst(root2,arr1)
    
    arr1.sort()
    # function call to finally convert merge array into bst...
    final_root = convert_array_to_bst(arr1)
    
    return final_root
    

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        if key < root.data:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    return root

## Driver code...!!!1
if __name__ == "__main__":
    root1 = root2 = None
     
    # Inserting values in first tree
    root1 = insert(root1, 100)
    root1 = insert(root1, 50)
    root1 = insert(root1, 300)
    root1 = insert(root1, 20)
    root1 = insert(root1, 70)
     
    # Inserting values in second tree
    root2 = insert(root2, 80)
    root2 = insert(root2, 40)
    root2 = insert(root2, 120)
    
    print("inorder traversal of bst1",inorder(root1))
    print()
    print("inorder traversal of bst1",inorder(root2))
    
    final_root = merge_bst(root1,root2)
    print()
    print("inorder traversal of merge bst",inorder(final_root))