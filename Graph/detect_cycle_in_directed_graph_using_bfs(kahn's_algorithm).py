
def iscyclic_using_toposort(N, adj):
        res = []
        topo = [0] * (N) 
        indegree = [0] * (N) 
        for i in range(N):          ## Get the indegree of the graph...
            for j in adj[i]:
                indegree[i] += 1 
            
        queue = []
        for i in range(N):
            if(indegree[i] == 0):
                queue.append(i)
            
        cnt = 0
        while len(queue) > 0: 
            node = queue.pop(0) 
            cnt =+ 1 
            for i in adj[node] :
                indegree[i] -= 1 
                if(indegree[i] == 0):
                    queue.append(i)
                
        if(cnt == N): ## it is DAG
            return False 
        return True

## Driver code....
if __name__ == "__main__":
    V = int(input())
    adj = [[] for i in range(V)]
    for i in range(V):
        u,v = list(map(int,input().split()))
        adj[u].append(v)
	## function call...!!!
    if (iscyclic_using_toposort(V,adj)):
        print("cyclic present")
    else:
        print("cycle is not present")
    
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