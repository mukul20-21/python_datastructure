def pivotelement(arr):
    start = 0
    mid = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if  arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid]
        elif (arr[mid] > arr[end]):
            start = mid+1
        else:
            end = mid-1
    return -1


## Driver code...!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print("pivot_element-->",pivotelement(arr))