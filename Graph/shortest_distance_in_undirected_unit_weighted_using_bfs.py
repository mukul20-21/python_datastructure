def bfs_distance(adj , N, src): 
    distance = [99999999] * (N) 
    queue = []
	
    distance[src] = 0
    queue.append(src) 

    while(len(queue)>0): 
        node = queue.pop(0) 
		
        for i in adj[node]:
            if(distance[node] + 1 < distance[i]):
                distance[i]=distance[node]+1
                queue.append(i)
		    
    return distance

## Driver code...
if __name__ == "__main__":
    V = int(input())
    adj = []
    for i in range(V):
        u = list(map(int,input().split()))
        adj.append(u)
    src = 0
    print(bfs_distance(adj,V,src))

"""
## index value of list is treat as vertex value for paricular node...
9
1 3
0 2 3
1 6 
0 4
3 5
4 6
2 5 7 8
6 8
6 7
"""
