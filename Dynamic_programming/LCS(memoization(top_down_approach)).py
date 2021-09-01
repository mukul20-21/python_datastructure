def LCS(X,Y,m,n):
    # base condition..
    if n ==0 or m ==0:
        return 0
    if t[m][n]!=-1:
        return t[m][n]
    # choice diagram..
    if (X[n-1] == Y[m-1]):
        t[m][n] = 1 + LCS(X,Y,m-1,n-1)
        return t[m][n]
    else:
        t[m][n] = max(LCS(X,Y,m,n-1),
                    LCS(X,Y,m-1,n))
        return t[m][n]

## Driver code..!!!
if __name__ == '__main__':
    ## n --> denoted for length of Y..(Columns)
    ## m --> denoted for length of X..(Rows)
    X = input()
    Y = input()
    n = len(Y)
    m = len(X)
    t = [[-1 for i in range(n+1)]for j in range(m+1)]
    print(LCS(X,Y,m,n))