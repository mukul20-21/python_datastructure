## jst follow the 4 steps of format define by aditiya verma..!!!

## utility function used into main calling function..!!
def ispalindrome(s):
    return s == s[::-1]

def solve(s,i,j):
    ## base condition...
    if (i>=j):
        return 0
    if (ispalindrome(s[i:j+1])):
        return 0
    if (t[i][j]!=-1):
        return t[i][j]
    ans = float('inf')
    ## Step3 and Step4...!!!!
    for k in range(i,j):
        # left subproblem...
        if (t[i][k]!=-1):
            left = t[i][k]
        else:
            left = solve(s,i,k)
        t[i][k] = left
        
        # right subproblem...
        if (t[k+1][j]!=-1):
            right = t[k+1][j]
        else:
            right = solve(s,k+1,j)
        t[k+1][j] = right
        ## jst avoid some more extra recursive calls..!!!
        temp_ans =(1 + left + right)
        ans = min(ans, temp_ans)
        
    t[i][j]=ans
    return t[i][j]

## Driver code...!!!!

if __name__ == '__main__':
    s = input()
    i = 0
    j = len(s)-1
    t = [[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
    print('minimum of partition',solve(s,i,j))