## modified binary search for early sorted array...!!!

def binary_search(arr,ele):
    start = 0
    mid = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if (ele == arr[mid]):
            return mid
        # check left constraint also..!!!
        if (mid-1>=start and ele == arr[mid-1]):
            return mid-1
        # check the right constraints also..!!!
        if (mid+1<=end and ele == arr[mid+1]):
            return mid+1
        elif(ele < arr[mid-1]):
            ## skip all three element
            end = mid-2
        else:
            start = mid+2
    return -1
        

## Driver code...!!!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    ele = int(input())
    print('index of given element is-->>>',binary_search(arr,ele))