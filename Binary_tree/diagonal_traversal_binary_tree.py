## Similar to verical order traversal jst with one variation...!!!
## root node level = 0
## level of right child nodes = same as parent node...
## level of left child nodes = +1 on parent node...

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None
        
def diagonal_traverse(root):
    if root is not None:
        dict = {}
        node_dict = {}
        que = list()
        que.append(root)
        node_dict[root.data] = 0
        while len(que) > 0:
            temp = []
            curr = que.pop(0)
            if curr is not None:
                level = node_dict[curr.data]
                if level in dict:
                    temp = dict.get(level)
                    temp.append(curr.data)
                else:
                    temp.append(curr.data)
                    dict[level] = temp

                if curr.left is not None:
                    left_node = curr.left
                    que.append(left_node)
                    node_dict[left_node.data] = node_dict[curr.data] +1
                if curr.right is not None:
                    right_node = curr.right
                    que.append(right_node)
                    node_dict[right_node.data] = node_dict[curr.data] 
        res = []
        for i in dict:
            res.append(dict[i])
        return res
        #print(dict)
        
if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    
    print(diagonal_traverse(root))