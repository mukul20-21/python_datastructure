def LCS(X,Y,n,m):
    # base condition..
    if n ==0 or m ==0:
        return 0
    
    # choice diagram..
    if (X[n-1] == Y[m-1]):
        return 1 + LCS(X,Y,n-1,m-1)
    else:
        return max(LCS(X,Y,n,m-1),
                    LCS(X,Y,n-1,m))

## Driver code..!!!
if __name__ == '__main__':
    X = input()
    Y = input()
    n = len(X)
    m = len(Y)
    print(LCS(X,Y,n,m))