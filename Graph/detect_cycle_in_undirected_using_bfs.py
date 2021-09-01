import sys
sys.stdout = open('/home/mukul/Documents/DSA_CP_QUESTION/output.txt','w')
sys.stdin = open('/home/mukul/Documents/DSA_CP_QUESTION/input.txt','r')



def isCyclicConnected(s, V, adj:list, visited:list):
	
	parent = [-1] * V
	queue = []
	visited[s] = True
	queue.append(s)
 
	while queue:
		u = queue.pop(0)
		for v in adj[u]:
			if not visited[v]:
				visited[v] = True
				queue.append(v)
				parent[v] = u
			elif parent[u] != v:
				return True
 
	return False


#Function to detect cycle in an undirected graph.
def iscycle(V, adj):
	#Code here
	visited = [False] * (V)
	for i in range(V):
		if not visited[i] and isCyclicConnected(i, V, adj, visited):
			return True
	return False

## Driver Code...!!!
if __name__ == "__main__":
    # V = no. of vertex.
	V = int(input())
	adj = []
	for i in range(V):
		v = list(map(int,input().split()))
		adj.append(v)
	## function call to check cycle is present or not..!!!
	
	if (iscycle(V, adj)):
		print("cycle is present")
	else:
		print("Not detect any cycle")
    
"""
sample input..
11 
2
1 4
5
2
3 10 16
5 7 
6 8
7 9 11
10 8
5 9
8
"""
