## same problem as mini deletion to get a string as palindrome..!!!
def min_insert(X,Y,m,n):
    t = [[-1 for i in range(n+1)] for j in range(m+1)]
    
    # base condition..!!1
    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j == 0):
                t[i][j] = 0
    
    ## convert base choice daigram into iterative approach..!!!
    for i in range(1,m+1):
        for j in range(1,n+1):
            if (X[i-1] == Y[j-1]):
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
                
    return m - t[m][n]
    
## driver code.....!!!!!
if __name__ == '__main__':
    X = input()
    Y = X[::-1]
    m = len(X)
    n = len(Y)
    print(min_insert(X,Y,m,n))    