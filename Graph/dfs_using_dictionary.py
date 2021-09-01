class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = {}
        
        for node in self.nodes:
            self.adj_list[node] = []
 
    def addEdge(self, u, v):
        self.adj_list[u].append(v)
 
    # A function used by DFS
    def Utility(self, v, visited,res):
 
        visited.add(v)
        res.append(v)
 
        for node in self.adj_list[v]:
            if node not in visited:
                self.Utility(node,visited,res)   ## recursive calls
 
 
    def DFS(self):
        visited = set()
 
        # Call the recursive helper function to print DFS traversal starting from all vertices one by one
        res = []
        for vertex in self.adj_list.keys():
            if vertex not in visited:
                self.Utility(vertex, visited,res)
        
        return res
 
 
# Driver code
# Create a graph given in the above diagram
nodes = [0,1,2,3]
edges = [(0, 1),(0, 2),(1, 2),(2, 0),(2, 3),(3, 3)]

g = Graph(nodes)
for u,v in edges:
    g.addEdge(u, v)

print ("Following is Depth First Traversal",g.DFS())
 