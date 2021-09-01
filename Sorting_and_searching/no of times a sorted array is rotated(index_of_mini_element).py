## no of times array rotate = index of minimum element..!!!!
def binary_search(arr):
    start = 0
    end = len(arr)-1
    mid = 0
    N=len(arr)
    
    while start<=end:
        mid = (start+end)//2
        ## if mid is minimum element..!!!
        ## to avoid corner cases..!!! dont jst used mid-1 and mid+1
        ## prev --> (mid+N-1)%N)
        ## next --> (mid+1)%N
        if (arr[mid]< arr[((mid+N-1)%N)] and arr[mid]<arr[((mid+1)%N)]):
            return mid
            
        elif(arr[mid] > arr[mid+1]):
            start = mid+1
        else:
            end = mid-1
    return -1

## driver code...!!!
if __name__ == '__main__':
    
    arr = list(map(int,input().split()))
    print('count of rotate array-->',binary_search(arr))