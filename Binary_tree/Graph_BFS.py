## here we use adjacency list for implementation of graph..

## function for traverse BFS for a graph using Deque

from collections import deque 

def BFS(adj,s):
    visited = [False] * len(adj)
    
    q = deque()
    q.append(s)
    
    visited[s] = True
    res = []
    while q:
        s = q.popleft()
        res.append(s)
        
        for u in adj[s]:
            if  visited[u] == False:
                q.append(u)
                visited[u] = True
    return res


## function to insert and print element into the adjacency list..

def  addedge(adj, u,v):
    adj[u].append(v)
    adj[v].append(u)


def  printlist(adj):
    for l in adj:
        print(l)
        

## Driver code::
V = 5
adj = [[] for i in range(V)]
addedge(adj,0,1)
addedge(adj,0,2)
addedge(adj,1,2)
addedge(adj,1,3)
addedge(adj,2,3)
addedge(adj,2,4)
addedge(adj,3,4)

printlist(adj)
## now call the bfs function..
s=0
print("Now BFS traverse of above graph is---",BFS(adj,s))



