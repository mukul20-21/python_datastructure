## completely same as lcs with a single line of code change..
def lc_substring(X,Y,m,n):
    t = [[-1 for i in range(n+1)] for j in range(m+1)]
    
    # base condition..!!1
    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j == 0):
                t[i][j] = 0
    
    ## convert base choice daigram into iterative approach..!!!
    ## jst replace the else condition with zero..
    ## remain all code is similar to (lenght of LCS)
    # To store the length of
    # longest common substring
    res = 0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if (X[i-1] == Y[j-1]):
                t[i][j] = 1 + t[i-1][j-1]
                # jst select the largest element from the total string
                res = max(res,t[i][j])
            else:
                t[i][j] =  0
    print( t )  
    return res
    
## driver code.....!!!!!
if __name__ == '__main__':
    X = input()
    Y = input()
    m = len(X)
    n = len(Y)
    print(lc_substring(X,Y,m,n))