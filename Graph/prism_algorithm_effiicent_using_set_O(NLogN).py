## here we use set intead of priority queue to get the minimum edge weight..
def mini_spanning_tree(adj,N):
    parent = [-1] * (N)
    key = [99999999] * (N)
    mstSet = [False]  *  (N)

    pq = set()

    key[0] = 0 
    parent[0] = -1 
    pq.add((0, 0))
    '''
    // Run the loop till all the nodes have been visited
    // because in the brute code we checked for mstSet[node] == false while computing the minimum
    // but here we simply take the minimal from the set, so a lot of times a node might be taken twice
    // hence its better to keep running till all the nodes have been taken. 
    '''
    while(pq):
        
        u = min(pq)[1] # return tuple 
        pq.remove(min(pq))
        
        
        mstSet[u] = True
        
        for  i in adj[u]: 
            v = i[0]
            weight = i[1]
            if (mstSet[v] == False and weight < key[v]):
                parent[v] = u
                key[v] = weight 
                pq.add((key[v], v))    
    
    return parent[1:],sum(key)
    

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
sample 1--
5 6
0 1 2
1 2 3
0 3 6
3 1 8
1 4 5
4 2 7

sample 2--
6 7 
0 1 5 
0 2 10 
0 3 100 
1 3 50 
1 4 200
3 4 250
4 5 50 
"""