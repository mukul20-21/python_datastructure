## utility function...!!!
# agr variable ko globally pass krna hai too likhna pdega nhi too list to direct bhi ho jayegi globally pass function m...

def findTopoSort(node, visited:list, stack, adj:list):
    visited[node] = 1
    for i in adj[node]: 
        if( not visited[i[0]]):
            findTopoSort(i[0], visited, stack, adj) 
        
    stack.append(node)


def shortestPath(src, N, adj:list): 
    visited = [0] * (N)
    stack = []
    for i in range(N): 
        if not visited[i]: 
            findTopoSort(i, visited, stack, adj) 
			
    distance = [99999999] * (N) 
    distance[src] = 0 

    while(len(stack)>0): 
       node = stack.pop() 
 
        if (distance[node] != 99999999):
            for i in adj[node]: 
                if(distance[node] + i[0] < distance[i[0]]): 
                    distance[i[0]] = distance[node] + i[1] 
		        
    return distance



## Driver code...!!!!
if __name__ == "__main__":
    Vertex,Edge = list(map(int,input().split()))
    adj = [[] for i in range(Vertex)] 
    for i in range(Edge):
	    u,v,wt = list(map(int,input().split()))
	    adj[u].append([v, wt])
    src = 0
    print(shortestPath(src, Vertex, adj)) 

"""
sample input with edges and weights..
6 8
0 1 2
0 4 1
1 2 3
2 3 6
3 0 0
4 2 2
4 5 4
5 3 1
"""