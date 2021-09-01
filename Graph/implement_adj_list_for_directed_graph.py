class Graph:
    def __init__(self,Nodes,is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        
        for node in self.nodes:
            self.adj_list[node] = []
            
    
    def add_egde(self,v,u):
        self.adj_list[u].append(v)
        if not  self.is_directed:
            self.adj_list[v].append(u)
    
    def print_graph(self):
        for node in self.nodes:
            print(node,"-->", self.adj_list[node])
            
## Driver code...!!!
nodes = [1,2,3,4,5]
all_edges = [(1,2),(2,3),(4,3),(3,5),(5,1),(1,3),(2,4)]

graph_obj = Graph(nodes,is_directed = True)

for u,v in all_edges:
    graph_obj.add_egde(u,v)

graph_obj.print_graph()
            