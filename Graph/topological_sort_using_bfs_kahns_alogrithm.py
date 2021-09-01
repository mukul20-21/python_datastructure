def topo(N, adj): 
    queue = [] 
    indegree = [0] * (N) 
    for i in range(N):
        for j in adj[i]: 
            indegree[j] += 1 
	        
    for i in range(N):
        if(indegree[i] == 0):
            queue.append(i)
	        
    topo = []
    cnt = 0
    while len(queue)>0: 
        node = queue.pop(0)
        topo.append(node)
        for i in adj[node]:
            indegree[i] -= 1
            if(indegree[i] == 0):
                queue.append(i) 
        cnt +=1
    if cnt != N:
        return False
    else:
        return topo


## Driver code....
if __name__ == "__main__":
    V = int(input())
    adj = [[] for i in range(V)]
    for i in range(V):
        u,v = list(map(int,input().split()))
        adj[u].append(v)
	## function call...!!!
    print(topo(V,adj))
    
"""
sample input of DAG
6
5 2
5 0
4 0
4 1
2 3
3 1
"""