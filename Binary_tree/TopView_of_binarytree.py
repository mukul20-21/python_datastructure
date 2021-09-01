class Node:
    def __init__ (self,data):
        self.data = data
        self.right = self.left = None
        
def top_view(root):
    if root is not None:
        dict = {}
        node_dict = {}
        que = list()
        que.append(root)
        node_dict[root.data] = 0
        while len(que) > 0:
            #temp = []
            curr = que.pop(0)
            if curr is not None:
                level = node_dict[curr.data]
                if level not in dict:
                    #temp.append(curr.data)
                    dict[level] = curr.data

                if curr.left is not None:
                    left_node = curr.left
                    que.append(left_node)
                    node_dict[left_node.data] = node_dict[curr.data] - 1
                if curr.right is not None:
                    right_node = curr.right
                    que.append(right_node)
                    node_dict[right_node.data] = node_dict[curr.data] + 1
        res = []
        for i in sorted(dict):
            res.append(dict[i])
        return res
    
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print(top_view(root))