## here the same function work for three problem together..!!
## 1st -- count_of_subset_sum
## 2nd -- count_no_of_subset_diff
## 3rd -- target_sum

def target_Sum(arr,diff):
    summ = (diff + sum(arr))//2
    n = len(arr)
    ## summ -- column , n -- row..
    t = [[0 for i in range(summ+1)] for j in range(n+1)]
    
    # initialize step..
    for i in range(n+1):
        for j in range(summ+1):
            if (i==0):
                t[i][j] = 0
            if (j==0):
                t[i][j] = 1
    
    # main code..
    ## n --> i , summ --> j ..
    for i in range(1,n+1):
        for j in range(summ+1):
            if (arr[i-1]<=j):
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
                
    return t[n][summ]


## driver code..!!!!

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    diff = int(input())
    print(target_Sum(arr,diff))