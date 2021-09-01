def dfs(node, parent, vis, tin, low, adj, timer, isArticulation): 
    vis[node] = 1
    timer +=1    
    tin[node] = low[node] = timer 
    child = 0 
    for it in adj[node]:
        if(it == parent): 
            continue 

        if(vis[it] == 0):
            dfs(it, node, vis, tin, low, adj, timer, isArticulation) 
            low[node] = min(low[node], low[it]) 

            if(low[it] >= tin[node] and parent != -1):
                isArticulation[node] = 1  
            child += 1
        else:
            low[node] = min(low[node], tin[it]) 
			
    if(parent != -1 and child > 1):
        isArticulation[node] = 1  

def printBridges(adj, n):

    vis = [0]*(n)               ## array for dfs
    tin = [-1]*(n)                      ## store time of insertion of every node..
    low = [-1]*(n)                      ## store lowest time of insertion..
 
    isArticulation = [0]*(n)
    timer = 0 
    
    for i in range(n):
        if(vis[i] == 0): 
            dfs(i, -1, vis, tin, low, adj, timer, isArticulation)
        	
    res = []
        
    for i in range(n):
        if(isArticulation[i] == 1):
            res.append(i) 
        
    return res
  

## Driver Code...!!!!
if __name__ == "__main__":
    V = int(input())
    adj = [[] for i in range(V)]
    for i in range(V):
        u,v = list(map(int,input().split()))
        adj[u].append(v)
        adj[v].append(u)
		
    print(printBridges(adj, V)) 
		
"""
5
0 1
0 2
1 2
1 3
3 4
"""