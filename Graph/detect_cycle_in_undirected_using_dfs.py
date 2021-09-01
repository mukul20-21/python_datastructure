def cyclic_component(u, parent, adj, visited):
        
    visited[u] = True
        
        #iterating on all the adjacent vertices.
    for v in adj[u]:
            
        if(v == parent):
            continue
        #if current vertex is visited, we return true else we call the function recursively to detect the cycle.
        elif(visited[v]):
            return True
        else:
            if(cyclic_component(v, u, adj, visited)):
                return True
    return False
        
    #Function to detect cycle in an undirected graph.
def iscycle(V, adj):
    #using a boolean list to mark all the vertices as not visited.
    visited = [False for i in range(V)]
 
    for i in range(V):
        if(visited[i] == False):
                if(cyclic_component(i, -1, adj, visited)):
                    return True
    return False

## Driver Code...!!!
if __name__ == "__main__":
    # V = no. of vertex.
	V = int(input())
	adj = []
	for i in range(V):
		v = list(map(int,input().split()))
		adj.append(v)
	## function call to check cycle is present or not..!!!
	
	if (iscycle(V, adj)):
		print("cycle is present")
	else:
		print("Not detect any cycle")
    
"""
sample input..
11 
2
1 4
5
2
3 10 16
5 7 
6 8
7 9 11
10 8
5 9
8
"""