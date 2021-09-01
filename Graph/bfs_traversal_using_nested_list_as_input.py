def bfsOfGraph(V, adj_list):
    # code here
    visited = [False] * (V + 1)
    # Create a queue for BFS
    queue = []
    bfs = []

    # Mark the source node as visited and enqueue it
    s = 0
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        bfs.append(u)

        for i in adj_list[u]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return bfs
        
## Driver Code...!!!
if __name__ == "__main__":
    # V = no. of vertex.
    # E = no. of edges.
    V,E = list(map(int,input().split()))
    adj = [[] for i in range(V)]
    for i in range(E):
        u,v = list(map(int,input().split()))
        adj[u].append(v)
    print(bfsOfGraph(V, adj))
    
"""
use this as a input...
5 4
0 1 
0 2
0 3 
2 4
"""
