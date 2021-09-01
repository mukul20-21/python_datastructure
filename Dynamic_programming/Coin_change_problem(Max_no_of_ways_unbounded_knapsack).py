# function to get the no. of ways in which we get the total
# sum using coin array..

## similar problem of 0/1 knapsack(count_of_subset_sum)
def coin_ways(coin,summ,n):
    
    t = [[0 for i in range(summ+1)] for j in range(n+1)]
    # initialization..!!!
    for i in range(n+1):
        for j in range(summ+1):
            if (i==0):
                t[i][j] = 0
            if (j == 0):
                t[i][j] = 1
    # code variation..!!! for unbounded knapsack..
    for i in range(1,n+1):
        for j in range(summ+1):
            if (coin[i-1]<=j):
                t[i][j] = (t[i-1][j] + t[i][j-coin[i-1]])
                # t[i-1][j] --> If not selected..
                # t[i][j-coin[i-1]] --> if coin get selected then it might select again..!!
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][summ]

## driver code..!!!!

if __name__ == '__main__':
    coin = list(map(int,input().split()))
    summ = int(input())
    n = len(coin)
    print(coin_ways(coin,summ,n))
    #print(t)