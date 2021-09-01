 ## maintain two array to keep track of dfs particular movement and visited vertex also..
 
def checkcycle( node, adj:list, visited:list, dfsvisited:list): 
    visited[node] = 1
    dfsvisited[node] = 1 
    
    for i in adj[node]: 
        if(visited[i] == 0): 
            if(checkcycle(i, adj, visited, dfsvisited) == True):
                return True 
        elif(dfsvisited[i] == 1):
                return True 
            
    dfsvisited[node] = 0
    return False


def iscyclic( adj:list, N):

    visited = [0] * (N) 
    dfsvisited = [0] * (N) 
        
    for i in range(N):
        if(visited[i] == 0):
            if(checkcycle(i, adj, visited, dfsvisited) == True):
                return True 
            
    return False

## Driver code..!!!
if __name__ == "__main__":
    V = int(input())
    adj = []
    for i in range(V):
        u = list(map(int,input().split()))
        adj.append(u)
	## function call...!!!
    if(iscyclic(adj, V)):
        print("YES, cycle is present in graph")
    else:
        print("No cycle detect")

"""
'''
sample input...
7
0 1
1 2
2 3
4 3
4 5
4 6
1 6
'''
"""