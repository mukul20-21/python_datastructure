def bellmanFord(edges, N, src):

    dist = [10000000] *(N)
        
    dist[src] = 0
    ## 0 --> u
    ## 1 --> v
    ## 2 --> wt
    for i in range(N-1): 
        for node in edges: 
            if(dist[node[0]] + node[2] < dist[node[1]]):
                dist[node[1]] = dist[node[0]] + node[2] 
    		
    for node in edges: 
        if(dist[node[0]] + node[2] < dist[node[1]]):
            print("Negative Cycle") 
            break
    
    print("shortest path from src=0 -->",dist)
    
        
   
## Driver code...!!!
if __name__ == "__main__":
    n,m= list(map(int,input().split()))
    adj = []
    for i in range(m):
        u,v,wt = list(map(int,input().split()))
        adj.append([u,v,wt])
    
    src = 0
    bellmanFord(adj, n, src)
		
"""
6 7
3 2 6
5 3 1
0 1 5
1 5 -3
1 2 -2
3 4 -2
2 4 3
"""