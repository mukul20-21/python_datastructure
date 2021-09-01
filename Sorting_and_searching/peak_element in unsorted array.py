## find the peak element in the unsorted array..!!!
## this question also similar to peak_element problem::
##          1. find the maximum element in bitonic array
 ##         2. search an element in bitonic array..!!
def peak_element(arr):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        ## if element between 0 and len-1 not on extreme position..
        if (mid > 0 and mid<len(arr)-1):
            if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid] < arr[mid-1]):
                end = mid-1
            else:
                start = mid+1
        elif(mid == 0):
            if (arr[mid]>arr[mid+1]):
                return 0
            else:
                return 1
        elif(mid == len(arr)-1):
            if (arr[mid]>arr[mid-1]):
                return mid
            else:
                return mid-1

## Driver code..!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(peak_element(arr))