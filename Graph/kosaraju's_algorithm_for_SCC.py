def dfs(node, st, adj, vis): 
    vis[node] = 1
    for it in adj[node]: 
        if(vis[it] == 0): 
            dfs(it, st, adj, vis); 
			
        st.append(node)

def revDfs(node, transpose:list, vis,res):
    vis[node] = 1
    res.append(node) 
    for it in transpose[node]: 
        if(vis[it] == 0): 
            revDfs(it, transpose, vis,res) 
			

def kosaRaju(adj, n):
    # step --1
    vis = [0]*(n) 
    st = [] 
    for i in range(n):
        if(vis[i] == 0):
            dfs(i, st, adj, vis) 
        	
    # step --2
    transpose = [[] for i in range(n)]
    for i in range(n):
        vis[i] = 0
        for it in adj[i]: 
            transpose[it].append(i) 
			
    # step--3
    while(st):
        node = st.pop() 
        res = []
        if(vis[node] == 0):
            revDfs(node, transpose, vis,res)
            print(res) 
           
            
## Driver code...!!!!
if __name__ == "__main__":
    
    V = int(input())
    adj = [[] for i in range(V)]
    for i in range(V):
        u,v = list(map(int,input().split()))
        adj[u].append(v)
			
	#function call..!!!	
    kosaRaju(adj, V) 
	
'''
5 
0 1 
1 2 
2 0 
1 3 
3 4 
'''