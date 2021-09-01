## Check the given string is scrambled or not..!!!
def solve(a: str,b : str):
    ## base case...!!!
    if (len(a) != len(b)):
        return False
    if (len(a)<=1):
        return False
    if (len(a)==0 and len(b) == 0):
        return True
    
    
    
    ## loop and extract ans from temp_ans..!!1
    n = len(a)
    #flag = False
    for i in range(1,n):
        if (solve(a[:i], b[:i]) and solve(a[i:], b[i:])):
            return True
        if (solve(a[-i:], b[:i]) and solve(a[:-i], b[i:])):
            return True
        '''
        if (solve(a[0:i],b[n-i:i]) and solve(a[i:n-i],b[0:i])): 
            flag = True
            break
          
        if (solve(a[0:i],b[0:i]) and solve(a[i:n-i],b[i:n-i])):
            flag = True
            break
            '''
    return False
## Driver code...!!!
if __name__ == '__main__':
    a = input()
    b = input()
    
    if (solve(a, b)):
        print("Yes")
    else:
        print("No")