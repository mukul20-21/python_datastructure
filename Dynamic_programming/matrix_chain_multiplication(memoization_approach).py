def solve(arr,i,j):
    ## Step2... find base condition..!!!
    if (i>=j):
        return 0
    if (t[i][j] != -1):
        return t[i][j]
    ## step3... find k loop scheme..!!!!
    mn = 999999
    for k in range(i,j,1):
        temp_ans = (solve(arr,i,k) + solve(arr,k+1,j) +
                    (arr[i-1]*arr[k]*arr[j]))  ## logic behind multiplication of matrix dimension..
    
    if (temp_ans < mn):
        mn = temp_ans
        t[i][j] = mn
    return t[i][j]
        


## Driver code...!!!1
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    t = [[-1 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
    ## step1... find valid value for i & j-->
    i = 1
    j = len(arr)-1
    print('minimum_cost--',solve(arr,i,j))