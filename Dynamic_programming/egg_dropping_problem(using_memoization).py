## create table to store the recursive calls of function...!!

def solve(e,f):
    ## base condition..!!
    if (f==0 or f == 1):
        return f
    if (e==1):
        return f
    if(t[e][f] != -1):
        return t[e][f]
    
    ## k loop and find ans using temp_ans
    ans = float('inf')
    for k in range(1,f):
        ## max function to get the worst cases..
        if(t[e-1][k-1] != -1):
            left = t[e-1][f-1]
        else:
            left = solve(e-1,k-1)
        t[e-1][k-1] = left
        
        if(t[e][f-k] != -1):
            right = t[e][f-k]
        else:
            right = solve(e,f-k)
        t[e][f-k] = right
        
        temp_ans = 1 + max(left,right)
        ## min function to get the minimum between all temp_ans
        ans = min(ans,temp_ans)
        t[e][f] = ans
        
    return t[e][f]
    
## Driver code..!!!
if __name__ == '__main__':
    e = int(input())
    f = int(input())
    t = [[-1 for i in range(f+1)] for j in range(e+1)]
    print('minimum_attempts-->',solve(e,f))