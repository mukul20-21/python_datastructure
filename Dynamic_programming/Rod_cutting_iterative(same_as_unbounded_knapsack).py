# Similarlity with 0/1 knapsack..
# wt[] --> length[] , val[] --> price[] , 
# W(weight of knapsack) --> N(length of rod) , 
# n (length of val[]) --> n(length of price[])

def rod_cutting(length,price,N,n):
    ## base condition..
    if n==0 or N == 0:
        return 0
    if (t[n][N] != -1):
        return t[n][N]
        
    ## choice diagram..!!!
    if (length[n-1]<=N):
        t[n][N] = max(price[n-1] + rod_cutting(length,price,N-length[n-1],n),
                        rod_cutting(length,price,N,n-1))
        return t[n][N]
    else:
        t[n][N] = rod_cutting(length,price,N,n-1)
        return t[n][N]

## driver code...

length = list(map(int,input().split()))
price = list(map(int,input().split()))
N = int(input())
n = len(price)
t = [[-1 for i in range(N+1)] for j in range(n+1)]
print(rod_cutting(length,price,N,n))