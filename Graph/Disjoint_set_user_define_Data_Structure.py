## define disjoint set to use two operation ---
# findparent() -- get the parent node of particular node.
# union() -- check weither given both nodes lies in same component or not..

def findparent(node):
    if node == parent[node]:
        return node
    
    return parent[node] = findparent(parent[node])

def Union(u,v):
    u = findparent(u)
    v = findparent(v)
    
    if (rank[u] < rank[v]):
        parent[u] = v
    elif (rank[v] < rank[u]):
        parent[v] = u
    else:
        parent[v] = u           ## if both rank is same increase any one in both nodes it all depand on us..
        rank[u] += 1
    

if __name__ == "__main__":
    m = int(input())
    
    parent = [-1] * (m)
    rank = [0] * (m)
    
    while m:
        u,v = list(map(int,input().split()))
        union(u,v)
        m -= 1
    
    print(parent)
    print(rank)