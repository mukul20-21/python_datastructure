class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adjj_list = {}
        
        for node in self.nodes:
            self.adjj_list[node] = []
            
    
    def add_egde(self,v,u):
        self.adjj_list[u].append(v)
        self.adjj_list[v].append(u)
         
def bfs_traverse(adj_list):
    visited = {}
    bfs = []
    queue = []
    
    for node in adj_list.keys():
        visited[node] = False
        
    s = 1
    visited[s] = True
    queue.append(s)
    
    while queue:
        u = queue.pop(0)
        bfs.append(u)
        
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    return bfs


## Driver code...!!!
nodes = [1,2,3,4,5,6,7]
all_edges = [(1,2),(2,3),(2,7),(3,5),(4,6),(5,7)]

graph_obj = Graph(nodes)
for u,v in all_edges:
    graph_obj.add_egde(u,v)

adj_list = graph_obj.adjj_list
level = {}
parent = {}
print(bfs_traverse(adj_list))

            