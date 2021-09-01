def print_lcs(X,Y,m,n):
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
        
    i = m 
    j = n
    string = ' '
    while(i>0 or j>0):
        if (X[i-1] == Y[j-1]):
            string+=X[i-1]
            i-=1
            j-=1
        else:       ## if element is not equal then jst select the max.
            if(t[i][j-1]>t[i-1][j]):
                j-=1
            else:
                i-=1
    return string[::-1]
    
## driver code.....!!!!!
if __name__ == '__main__':
    X = input()
    Y = input()
    m = len(X)
    n = len(Y)
    print(print_lcs(X,Y,m,n))