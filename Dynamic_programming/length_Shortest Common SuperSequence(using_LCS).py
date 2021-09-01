## same code hai h lcs wla bs last m length of supersequence find krne k krna total lenth se LCS ki lenth minus krde..!!! 

def length_SCS(X,Y,m,n):
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
        
        return ((m+n)-t[m][n])
## driver code.....!!!!!
if __name__ == '__main__':
    X = input()
    Y = input()
    m = len(X)
    n = len(Y)
    print(length_SCS(X,Y,m,n))           