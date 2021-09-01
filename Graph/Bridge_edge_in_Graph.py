def dfs(node, parent, visited, tin, low, adj:list, timer,res):
    visited[node] = 1 
    timer += 1
    tin[node] = low[node] = timer

    for it in adj[node]: 
        if(it == parent): 
            continue 

        if(visited[it] == 0): 
            dfs(it, node, visited, tin, low, adj, timer,res) 
            low[node] = min(low[node], low[it]) 

            if(low[it] > tin[node]):                ## check bridge condition if exist..
                res.append([it ,node]) 
				
        else:
            low[node] = min(low[node], tin[it]) 
	
def printBridges(adj, n):

    visited = [0]*(n)               ## array for dfs
    tin = [-1]*(n)                      ## store time of insertion of every node..
    low = [-1]*(n)                      ## store lowest time of insertion..

    timer = 0
    res = []
    for i in range(n): 
        if(visited[i] == 0):
            dfs(i, -1, visited, tin, low, adj, timer,res) 
    
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