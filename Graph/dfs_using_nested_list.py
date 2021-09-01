def dfs(visited, graph, node,res):
    if node not in visited:
        res.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            
            dfs(visited, graph, neighbour,res)
            

#Function to return a list containing the DFS traversal of the graph.
def dfsOfGraph(adj):
    visited = set()
    res = []
     # pass 0 as a source node..   
    dfs(visited,adj,0,res)
        
    return res
    
## Driver code..!!!!!!!
if __name__ == "__main__":
    # V = no. of vertex.
    # E = no. of edges.
    V,E = list(map(int,input().split()))
    adj = [[] for i in range(V)]
    for i in range(E):
        u,v = list(map(int,input().split()))
        adj[u].append(v)
    print(dfsOfGraph(adj))
    
"""
sample input..
5 4
0 1 
0 2
0 3 
2 4
"""
