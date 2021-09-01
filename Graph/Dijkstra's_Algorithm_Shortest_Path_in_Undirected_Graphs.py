
def  shortest_path(src, N,adj):

    distance = [99999999] *(N+1)
        
    distance[src] = 0 
        
    s = set()
    s.add((src,0))    ## insert element in set as [vertex,weight]
    # 0 --> show first element of tuple means vertex
    # 1 --> show second element of tuple means weight
   
    while(s): 
        node = min(s) # return tuple
        s.remove(min(s))
         
        for i in  adj[node[0]]:
            if (distance[node[0]] + i[1] < distance[i[0]]) :        ## distance array element + current weight < already exist element in distance array.
                                                                                            
                    distance[i[0]] = distance[node[0]] + i[1]           ## update the value with above value in distance array.
                    s.add((i[0], distance[i[0]]))                               ## once value are update make pair (vertex,weight) of update in set
              
    return distance
        
     
## Driver code...!!!!
if __name__ == "__main__":
    Vertex, Edge = list(map(int,input().split()))
    adj = [[] for i in range(Vertex+1)]
    for i in range(Vertex):
        u,v,wt = list(map(int,input().split()))
        adj[u].append([v,wt])                   # undirected graph 
        adj[v].append([u,wt])
    src = 1
    
    print(shortest_path(src,Vertex,adj))
    
'''
sample input..
4 4 
1 2 24
1 4 20
3 1 3
4 3 12
'''
