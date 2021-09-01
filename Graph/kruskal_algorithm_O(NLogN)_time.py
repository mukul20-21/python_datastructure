## utility function to implement kruskal algorithm...
def findPar( u, parent:list):
    if(u==parent[u]):
        return u
    parent[u] = findPar(parent[u], parent) 
    return parent[u]
    
def union(u, v, parent:list,rank:list): 
    u = findPar(u, parent) 
    v = findPar(v, parent)
    
    if(rank[u] < rank[v]):
        parent[u] = v
    elif(rank[v] < rank[u]): 
        parent[v] = u 
    else:
        parent[v] = u
        rank[u] += 1 
        
def KruskalAlgo(adj, N):
    
    sorted(adj, key =lambda x: x[2])                ## sorted edge wrt to weight...
        
    parent = []
    rank = []
    for i in range(N):
        parent.append(i) 
        rank.append(0)
        
    costMst = 0
    mst = []
    for i in adj:                           ## greedy approach to check each edge one by one...
        if(findPar(i[0], parent) != findPar(i[1], parent)):
            costMst += i[2] 
            mst.append(i) 
            union(i[0], i[1], parent, rank) 
    
    return costMst,mst    ## written minimum weight and edges of mst...
        
  
if __name__ == "__main__":
    V = int(input())
    adj = []
    for i in range(V):
        temp = list(map(int,input().split()))
        adj.append(temp)
        
    print(KruskalAlgo(adj, V))
	
"""
sample input
6
0 1 2
0 3 6
1 3 8
1 2 3
1 4 5
2 4 7
"""