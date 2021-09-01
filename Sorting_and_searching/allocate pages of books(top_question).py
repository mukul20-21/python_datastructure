## utility function..!!!
def isvalid(arr,n,k,mid):
    student = 1
    summ = 0
    for i in range(n):
        summ+=arr[i]
        if(summ>mid):
            student+=1
            summ = arr[i] ## assign element to next student..
        if(student>k):
            return False
    return True

## function to get the minimum pages allocated to a student..
def min_page(arr,k):
    start = max(arr)
    end = sum(arr)
    n = len(arr)
    res = -1
    ## if no of student is greater than no of books..!!!
    if (n<k):
        return -1
    while start<=end:
        mid = (start+end)//2
        ## check the mid element fullfil the condition of no. of student
        if (isvalid(arr,n,k,mid)==True):
            res = mid
            end = mid-1
        else:
            start = mid+1
    return -1
    
    
## Driver code..!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    k = int(input())
    
    print('minimum no of pages..!!!',min_page(arr,k))