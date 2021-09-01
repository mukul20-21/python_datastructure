## same code but an additional table to avoid repeative same recursive calls

def solve(s,i,j,istrue):
    ## step2 -->base condition..!!!!
    if (i > j):
        return 0
    if (i == j):
        if (istrue == 1):
            return 1 if s[i] == 'T' else 0
        else:
            return 1 if s[i] == 'F' else 0
    if (t[i][j][istrue] != -1):
        return t[i][j][istrue]
    
    ## step3 & 4 --> find k range and function to find ans from temp_ans..!!!
    ans = 0
    for k in range(i+1,j,2):
        # lt --> left-True , lf --> left-False
        # rt --> right-True , rf --> right-False
        ## this are the temp_ans
        if(t[i][k-1][1] != -1):
            lt = t[i][k-1][1]
        else:
            lt = solve(s, i, k-1, 1)
        t[i][k-1][1] = lt
        
        if (t[i][k-1][0] != -1):
            lf = t[i][k-1][0]
        else:
            lf = solve(s, i, k-1, 0)
        t[i][k-1][0] = lf
        
        if (t[k+1][j][1] != -1):
            rt = t[k+1][j][1]
        else:
            rt = solve(s, k+1, j, 1)
        t[k+1][j][1] = rt
        
        if (t[k+1][j][0] != -1):
            rf = t[k+1][j][0]
        else:
            rf = solve(s, k+1, j, 0)
        t[k+1][j][0] = rf
        
        ## condition to find the final_ans..
        ## AND operator..
        if (s[k] == '&'):
            if(istrue == 1):
                ans += (lt*rt)
            else:
                ans += (lf*rt) + (lf*rf) + (lt*rf)
        ## OR operator..
        elif(s[k] == '|'):
            if(istrue == 1):
                ans += (lt*rt) + (rt*lf) + (rf*lt)
            else:
                ans += (lf*rf)
        ## XOR operator..
        elif(s[k] == '^'):
            if(istrue == 1):
                ans += (lt*rf) + (rt*lf)
            else:
                ans += (rt*lt) + (rf*lf)
        t[i][j][istrue] = ans
        
    return ans

## Driver code..!!!!
if __name__ == '__main__':
    s = input()
    ## step1 --> initialize i & j value..
    i = 0
    j = len(s)-1
    istrue = 1
    t = [[[-1 for k in range(2)] for i in range(len(s)+1)] for j in range(len(s)+1)]
    print('No of ways to be true--',solve(s,i,j,istrue))