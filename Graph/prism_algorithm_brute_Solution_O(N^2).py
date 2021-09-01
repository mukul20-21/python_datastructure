def mini_spanning_tree(adj,N):
    parent = [-1]*(N)
    key = [99999999]*(N)
    mstSet = [False]*(N) 
 
    key[0] = 0
    parent[0] = -1 
 
    for count in range(N-1):
        mini = 99999999 
        u = 0 
  
        for v in range(N):              ## check for the minimal value again key array after avoid previous used node..
            if (mstSet[v] == False and key[v] < mini):                  ## to avoid this we also use set data structure here..
                mini = key[v] 
                u = v 
                
        mstSet[u] = True 
        
        for i in adj[u]:                ## iterate for all adjacent node and keep on updating parent and key
            vert = i[0]
            weight = i[1]
            if (mstSet[vert] == False and weight < key[vert]): 
                parent[vert] = u 
                key[vert] = weight 
    
    return parent[1:],sum(key)              ## key array return the minimum weights
    

## Driver code...!!!
if __name__ == "__main__":
    vertex ,edge = list(map(int,input().split()))
    adj = [[] for i in range(vertex)]
    for i in range(edge):
        a,b,wt = list(map(int,input().split())) 
        adj[a].append([b,wt])
        adj[b].append([a,wt])
    
    mst_edge,weight = mini_spanning_tree(adj,vertex)
    print("node include in mst",mst_edge,"\n minimum weight-->",weight)

"""
5 6
0 1 2
1 2 3
0 3 6
3 1 8
1 4 5
4 2 7
"""