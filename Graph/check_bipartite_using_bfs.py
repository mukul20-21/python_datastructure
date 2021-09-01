
def bipartiteBfs(src, adj, color):
    q = []
    q.append(src) 
    color[src] = 1 
    while q: 
        node = q[0] 
        q.pop(0)
        
        for it in adj[node]:
        
            if(color[it] == -1):
                color[it] = 1 - color[node] 
                q.append(it)
            elif(color[it] == color[node]): 
                return False
    return True

def  checkBipartite(adj:list, n):

    color = [-1] *(n)
    
    for i in range(n): 
        if(color[i] == -1):
            if not bipartiteBfs(i, adj, color): 
                return False
    return True

## Driver code...!!!!
if __name__ == "__main__":
    V = int(input())
    adj = []
    for i in range(V):
        u = list(map(int,input().split()))
        adj.append(u)
	## function call...!!!
    if(checkBipartite(adj, V)):
        print("YES")
    else:
        print("NO")
        

'''
sample input...
9
8 7
0 1
1 2
2 3
3 4
4 6
6 7
1 7
4 5
'''
