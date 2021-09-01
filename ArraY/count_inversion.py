## using merge sort and slightly modified it to get result...
## while merging array we check our count inversion condition and increase count pointer...

## function to count inversion while merging..
def merge(arr, temp, left, mid , right):
    i,j,k = 0,0,0
    count = 0

    i = left ## i is index of left subarray..
    j = mid ## j is index of right subarray.. because we split from mid then array also start from mid..
    k = left ## k is index of resultant merging subarray..

    while i<=mid-1 and j<= right:
        if arr[i] <= arr[j]: # checking the inversion condition..
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            k+=1
            j+=1
            ## here we add all left value which is lesser than right array jth value..
            count = count + (mid-i)

    ## remaining element...
    while (i <= mid-1):
        temp[k] = arr[i]
        k+=1
        i+=1

    while (j <= right):
        temp[k] = arr[j]
        k+=1
        j+=1

    for i in range(left,right+1):
        arr[i] = temp[i]

    return count


# function to split the array using recursion...!!!!
def mergesort(arr:list,temp:list,left , right):
    mid = 0
    inv_count = 0
    if right>left:
        mid = (left+right)//2

        inv_count += mergesort(arr,temp,left,mid)  ## split left array
        inv_count += mergesort(arr,temp,mid+1,right) ## split right array..

        inv_count += merge(arr,temp, left, mid+1, right)

    return inv_count




## Driver code...!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    temp = [0]*len(arr)
    ans = mergesort(arr,temp,0,len(arr)-1)
    print('total inversion count-->',ans)


'''
sample input..
5 3 2 4 1
'''
