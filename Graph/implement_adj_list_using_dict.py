class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = {}
        
        for node in self.nodes:
            self.adj_list[node] = []
            
    
    def add_egde(self,v,u):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def print_graph(self):
        for node in self.nodes:
            print(node,"-->", self.adj_list[node])
            
## Driver code...!!!
nodes = [1,2,3,4,5]
all_edges = [(1,2),(2,3),(4,3),(3,5),(5,1),(1,3),(2,4)]

graph_obj = Graph(nodes)
for u,v in all_edges:
    graph_obj.add_egde(u,v)

graph_obj.print_graph()
            