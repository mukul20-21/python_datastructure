## approach..
#1. find the middle element of sorted array and make that element as a root node.
#2. once root created calls recursively for left and right subtree with arr element smaller than middle element and greater than middle element..
#3. after conversion print preorder traversal of tree..

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
    
    
"""
1)Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.
time complexity == O(n)
space complexity == O(1)


"""