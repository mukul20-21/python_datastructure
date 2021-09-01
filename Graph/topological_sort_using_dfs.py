def findTopoSort( node, visited, adj, stack): 
    visited[node] = 1 
    
    for i in adj[node]: 
        if(visited[i] == 0): 
            findTopoSort(i, visited, adj, stack)
    
    stack.append(node) 
        
 
def topoSort(N, adj):
    stack = [] 
    visited = [0] * (N+1)
        
    for i in range(N):
        if(visited[i] == 0):
            findTopoSort(i, visited, adj, stack)
            
    return stack[::-1]           # return in reverse order because last element append at the last position...
 
## Driver code...!!! 
if __name__ == "__main__":
    V = int(input())
    adj = [[] for i in range(V)]
    for i in range(V):
        u,v = list(map(int,input().split()))
        adj[u].append(v)
	## function call...!!!
    print(topoSort(V,adj))
    
"""
sample input of DAG
4
3 4
3 0
1 0
2 0
"""