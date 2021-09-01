import sys
def minimum_subset_sum_diff(arr,n):
    summ = sum(arr)
    t = [[False for i in range(summ+1)] for j in range(n+1)]
    ## initialization step--
    for i in range(n+1):
        for j in range(summ+1):
            if (i==0):
                t[i][j] = False
            if (j==0):
                t[i][j] = True
    ## code conversion from 0/1 knapsack to subset_sum
    ## if only one array is given than jst avoid the val array..
    for i in range(n+1):
        for j in range(summ+1):
            if (arr[i-1]<=j):
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            elif(arr[i-1]>j):
                t[i][j] = t[i-1][j]

    # initial the element with maximum value present in given array..
    diff = summ
    
    # run the loop in last row of matrix to find the minimum element diff..
    # summ -- column of matrix and we have to select half of it..
    for j in range(summ//2,-1,-1):
        if (t[n][j] == True):
            diff = summ - (2*j)
            break
    return diff    
    


## Driver code...!!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    n = len(arr)
    print(minimum_subset_sum_diff(arr,n))