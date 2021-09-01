## get the count of mini no of coin..
# which is required to get the given summ..
## This problem totally based on 0/1 knapsack...

# coin --> weight , m --> W , n = length of coin array..
import sys
import math
def coin_change(coin,m,n):
    t = [[-1 for i in range(m+1)] for j in range(n+1)]
    # initialization step..
    inf = sys.maxsize
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                t[i][j] = inf-1
            if j == 0:
                t[i][j] = 0
    for j in range(1,m+1):
        if (j%coin[0]==0):
            t[i][j] = j//coin[0]
        else:
            t[i][j] = inf-1
    
    ## code based on 0/1 knapsack..
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (coin[i-1]<=j):
                t[i][j] = min(t[i][j-coin[i-1]]+1 , t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    if t[n][m] == 9223372036854775806:
        return -1
    else:        
        return t[n][m]
    #print(t)

## driver code...!!!
if __name__ == '__main__':
    coin = list(map(int,input().split()))
    m = int(input())
    n = len(coin)
    #res,t = coin_change(coin,m,n)
    print('minimum no of coins to get the sum:--',coin_change(coin,m,n))