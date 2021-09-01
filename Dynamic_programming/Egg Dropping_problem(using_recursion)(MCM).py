## find the count of minimun attempts for getting worst case to find threshold floor..!!
## threshold floor --> that first floor were egg is not broken down after fall..

## main point --> humko minimum no of count likhane hai worst case k liye..!!!

def solve(e,f):
    ## base condition..!!
    if (f==0 or f == 1):
        return f
    if (e==1):
        return f
    
    ## k loop and find ans using temp_ans
    ans = float('inf')
    for k in range(1,f):
        ## max function to get the worst cases..
        temp_ans = 1 + max(solve(e-1,k-1),solve(e,f-k))
        ## min function to get the minimum between all temp_ans
        ans = min(ans,temp_ans)
        
    return ans
    
## Driver code..!!!
if __name__ == '__main__':
    e = int(input())
    f = int(input())
    print('minimum_attempts-->',solve(e,f))