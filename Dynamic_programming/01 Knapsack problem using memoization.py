## add table t to recursive solution to convert into memoization...!!!!

def knapsack(weight,value,w,n):
    ## base condition..
    if n == 0 or w == 0:
        return 0
    if (t[n][w] != -1):
        return t[n][w]
    ## choice diagram..
    if (weight[n-1]<=w):
        t[n][w]=max(value[n-1]+knapsack(weight,value,w-weight[n-1],n-1),
                                knapsack(weight,value,w,n-1))
        return t[n][w]
    elif (weight[n-1]>w):
        t[n][w]=(knapsack(weight,value,w,n-1))
        return t[n][w]

if __name__ == '__main__':
    
    weight = list(map(int,input().split()))
    value = list(map(int,input().split()))
    w = int(input())
    n = len(value)
    ## w = rows, n = columns....
    t = [ [-1 for i in range(w+1)] for j in range(n+1) ]
    print(knapsack(weight,value,w,n))