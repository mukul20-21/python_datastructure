class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        

def sorted_array(nums):
    if not nums:
        return

    mid = len(nums)//2
    
    root = Node(nums[mid])
    root.left = sorted_array(nums[:mid])
    root.right = sorted_array(nums[mid+1:])
    
    return root

def utility(root,res):
    if root is None:
        return 
    res.append(root.data)
    utility(root.left,res)
    utility(root.right,res)

def preorder(root):
    res = []
    utility(root,res)
    return res


def sortedArrayToBST(nums):
    root = sorted_array(nums)
    return preorder(root)
    
    
### Driver code..!!!!
if __name__ == "__main__":
    nums = [-5 ,-2 ,-2 ,1 ,1 ,1 ,5 ,7]
    print("BST after convert",sortedArrayToBST(nums))