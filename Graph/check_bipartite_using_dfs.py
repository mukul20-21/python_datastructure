def dfscheck(adj:list, node, color:list):
    for i in adj[node]:
        if(color[i] == -1):
            color[i] = 1 - color[node] 

            if not dfscheck(adj, i, color):   ## recursive call after changing value of color array..
                return False 
        elif(color[i] == color[node]):
            return False
    return True


def checkBipartite( adj,  n):           # take adjacent list and no of vertex as a input..
    color = [-1] * (n)
    for i in range(n):
        if(color[i] == -1):
            if( not dfscheck(adj, i, color)):
                return False 
        
    return True 

## Driver Code...!!!

if __name__ == "__main__":
    V = int(input())
    adj = []
    for i in range(V):
        u = list(map(int,input().split()))
        adj.append(u)
	## function call...!!!
    if(checkBipartite(adj, V)):
        print("YES, it is bipartite graph")
    else:
        print("Not a bipartite graph")

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