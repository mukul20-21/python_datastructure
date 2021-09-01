## the function return the no. of ways from which we get the True boolean output..

def solve(s,i,j,istrue):
    ## step2 -->base condition..!!!!
    if (i > j):
        return 0
    if (i == j):
        if (istrue == 1):
            if s[i] == 'T':
                return 1
            else:
                return 0
        else:
            if s[i] == 'F':
                return 1
            else:
                return 0
           
    
    ## step3 & 4 --> find k range and function to find ans from temp_ans..!!!
    ans = 0
    for k in range(i+1,j,2):
        # lt --> left-True , lf --> left-False
        # rt --> right-True , rf --> right-False
        ## this are the temp_ans
        lt = solve(s, i, k-1, 1)
        lf = solve(s, i, k-1, 0)
        rt = solve(s, k+1, j, 1)
        rf = solve(s, k+1, j, 0)
        
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
    
    return ans

## Driver code..!!!!
if __name__ == '__main__':
    s = input()
    ## step1 --> initialize i & j value..
    i = 0
    j = len(s)-1
    istrue = 1
    print('No of ways to be true--',solve(s,i,j,istrue))