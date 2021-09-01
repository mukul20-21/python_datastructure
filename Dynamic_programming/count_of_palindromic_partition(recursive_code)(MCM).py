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
    ans = float('inf')
    ## Step3 and Step4...!!!!
    for k in range(i,j):
        temp_ans =(1 + solve(s,i,k) + solve(s,k+1,j))
        ans = min(ans, temp_ans)
        
    return ans

## Driver code...!!!!

if __name__ == '__main__':
    s = input()
    i = 0
    j = len(s)-1
    print('minimum of partition',solve(s,i,j))