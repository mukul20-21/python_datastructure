class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def get_array_inorder(root,res):
    if root is None:
        return
    get_array_inorder(root.left,res)
    res.append(root.data)
    get_array_inorder(root.right,res)
    
def array_to_balance_bst(nums):
    if not nums:
        return
    
    mid = len(nums)//2
    root = Node(nums[mid])
    root.left = array_to_balance_bst(nums[:mid])
    root.right = array_to_balance_bst(nums[mid+1:])
    
    return root
def convert_bst_to_balance_bst(root):
    res = []
    ## get sorted array
    get_array_inorder(root,res)
    #nprint(res)
    final_root = array_to_balance_bst(res)
    return final_root

def preorder(root):
    if root is None:
        return 
    print(root.data,end = " ")
    preorder(root.left)
    preorder(root.right)


## Driver code..!!!
if __name__ == "__main__":
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)
    root.left.left.left = Node(8)
    root.left.left.left.left = Node(7)
    root.left.left.left.left.left = Node(6)
    root.left.left.left.left.left.left = Node(5)
    
    print("preorder traversal before conversion",preorder(root))
    
    after_convert_root=convert_bst_to_balance_bst(root)
    
    print("preorder traversal after conversion",preorder(after_convert_root))