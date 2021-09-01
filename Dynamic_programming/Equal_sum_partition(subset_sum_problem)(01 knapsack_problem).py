## Its jst small variation of previous subset_sum problem..
def Equal_sum_partition(arr,n):
    arr_sum = sum(arr)
    if arr_sum%2!=0:
        return False
    else:
        return subset_sum(arr,arr_sum//2,n)
        
        
## subset_sum function return is subset present in the array...!!!!
def subset_sum(arr,summ,n):
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
    
    return t[n][summ]
    
    
## Driver code...!!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    n = len(arr)
    print(Equal_sum_partition(arr,n))